import sqlite3


class RecordNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(f'Record not found: {message}')


class DbCommitException(Exception):
    def __init__(self, message):
        super().__init__(f'Db commit error: {message}')


class DbUpdateException(Exception):
    def __init__(self, message):
        super().__init__(f'Db update error: {message}')


class DbDeleteException(Exception):
    def __init__(self, message):
        super().__init__(f'Db delete error: {message}')


class PlayerMapper:
    """ Save player states like:
        score, level
    """

    QUERIES = {
        'get': """SELECT IDPLAYER, NAME, SCORE, LEVEL
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
            return result[0]
        else:
            raise RecordNotFoundException(f'Player {name} not found')

    def create(self, name: str):
        query = self.QUERIES['create'].format(player_name=name)
        self.cursor.execute(query)
        try:
            self.connection.commit()
        except Exception as e:
            raise DbCommitException(e.args)

    def update(self, name: str, score: int, level: int):
        params = {
            'player_name': name,
            'score': score,
            'level': level,
        }
        query = self.QUERIES['update'].format(**params)
        self.cursor.execute(query)
        try:
            self.connection.commit()
        except Exception as e:
            raise DbUpdateException(e.args)

    def delete(self, name):
        query = self.QUERIES['delete'].format(player_name=name)
        self.cursor.execute(query)
        try:
            self.connection.commit()
        except Exception as e:
            raise DbDeleteException(e.args)


if __name__ == '__main__':
    # For tests
    import os

    from db import DB_cretor

    # Create db
    db = DB_cretor('test_db.sqlite')
    test_db_name = db.create_db()
    player_mapper = PlayerMapper(test_db_name)
    # Create player
    player_data = player_mapper.create('Cyxapic')
    # Get player from DB
    player_data = player_mapper.get('Cyxapic')
    assert player_data == (1, 'Cyxapic', 0, 1)
    # Print player data
    print(player_data)

    # Update player
    player_data = player_mapper.update('Cyxapic', 100, 2)
    player_data = player_mapper.get('Cyxapic')
    assert player_data == (1, 'Cyxapic', 100, 2)
    # Print player data
    print(player_data)
    player_data = player_mapper.delete('Cyxapic')
    assert player_data is None
    os.remove(test_db_name)
