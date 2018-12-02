import os
import sqlite3


class DB_cretor:
    """ Create DB sqlite3 with giving name
        name -- str; Name DB file
    """
    query = """
        PRAGMA foreign_keys = off;
        BEGIN TRANSACTION;

        DROP TABLE IF EXISTS players;
        CREATE TABLE players (
            idplayer INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
            name VARCHAR (32) NOT NULL UNIQUE,
            score INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1
        );

        COMMIT TRANSACTION;
        PRAGMA foreign_keys = on;
    """

    def __init__(self, name):
        self.name = name
        self._create_db_file()

    def create_db(self):
        con = sqlite3.connect(self.name)
        cur = con.cursor()
        cur.executescript(self.query)
        cur.close()
        con.close()
        return self.name

    def _create_db_file(self):
        if not os.path.exists(self.name):
            os.mknod(self.name)
