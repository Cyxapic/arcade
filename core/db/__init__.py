from core.settings import configurator

from .db_mapper import UnitOfWork, PlayerDB, PlayerMapper
from .db import DB_cretor


DB_NAME = configurator.db_name

db_creator = DB_cretor


def mapper(): return PlayerMapper(DB_NAME)


player_mapper = PlayerMapper
unitof_work = UnitOfWork
player_db = PlayerDB
