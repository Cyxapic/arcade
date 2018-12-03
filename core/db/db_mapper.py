import sqlite3
import threading

from .exceptions import (RecordNotFoundException,
                         DbCommitException,
                         DbUpdateException,
                         DbDeleteException)


class PlayerMapper:
    """ Save player states like:
        score, level
    """

    QUERIES = {
        'get': """SELECT NAME, SCORE, LEVEL
                  FROM PLAYERS WHERE NAME='{player_name}'""",
        'create': """INSERT INTO PLAYERS (NAME) VALUES('{player_name}')""",
        'update': """UPDATE PLAYERS SET SCORE='{score}', LEVEL='{level}'
                     WHERE NAME='{player_name}'""",
        'delete': """DELETE FROM PLAYERS WHERE NAME='{player_name}'"""
    }

    def __init__(self, db_name: str):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def get(self, name):
        query = self.QUERIES['get'].format(player_name=name)
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if result:
            return PlayerDB(*result[0])
        else:
            raise RecordNotFoundException(f'Player {name} not found')

    def create(self, player):
        query = self.QUERIES['create'].format(player_name=player.name)
        self.cursor.execute(query)
        try:
            self.connection.commit()
        except Exception as e:
            raise DbCommitException({e.args})

    def update(self, player):
        params = {
            'player_name': player.name,
            'score': player.score,
            'level': player.level,
        }
        query = self.QUERIES['update'].format(**params)
        self.cursor.execute(query)
        try:
            self.connection.commit()
        except Exception as e:
            raise DbUpdateException({e.args})

    def delete(self, name):
        query = self.QUERIES['delete'].format(player_name=name)
        self.cursor.execute(query)
        try:
            self.connection.commit()
        except Exception as e:
            raise DbDeleteException({e.args})


class UnitOfWork:
    """
    Паттерн UNIT OF WORK
    """
    current = threading.local()

    def __init__(self, mapper):
        self.new_objects = set()
        self.dirty_objects = set()
        self.removed_objects = set()
        self.mapper = mapper

    def register_new(self, obj):
        self.new_objects.add(obj)

    def register_dirty(self, obj):
        self.dirty_objects.add(obj)

    def register_removed(self, obj):
        self.removed_objects.add(obj)

    def commit(self):
        self.insert_new()
        self.update_dirty()
        self.delete_removed()

    def insert_new(self):
        for obj in self.new_objects:
            self.mapper().create(obj)

    def update_dirty(self):
        for obj in self.dirty_objects:
            self.mapper().update(obj)

    def delete_removed(self):
        for obj in self.removed_objects:
            self.mapper().delete(obj)

    @staticmethod
    def new_current(mapper):
        __class__.set_current(UnitOfWork(mapper))

    @classmethod
    def set_current(cls, unit_of_work):
        cls.current.unit_of_work = unit_of_work

    @classmethod
    def get_current(cls):
        return cls.current.unit_of_work


class DomainObject:
    def mark_new(self):
        UnitOfWork.get_current().register_new(self)

    def mark_dirty(self):
        UnitOfWork.get_current().register_dirty(self)

    def mark_removed(self):
        UnitOfWork.get_current().register_removed(self)


class PlayerDB(DomainObject):
    def __init__(self, name: str, score=0, level=1):
        self.name = name
        self.score = score
        self.level = level
