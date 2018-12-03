import os

from core.db import (db_creator,
                     mapper,
                     player_mapper,
                     unitof_work,
                     player_db)


# For tests ******************************************
if __name__ == '__main__':
    DB_NAME = db_creator('game.sqlite').create_db()
    pl_mapper = player_mapper(DB_NAME)

    pl_mapper.create(player_db('Igor'))
    pl_mapper.create(player_db('Fedor'))

    try:
        unitof_work.new_current(mapper)
        new_player_1 = player_db('Igor')
        new_player_1.mark_new()

        new_player_2 = player_db('Fedor')
        new_player_2.mark_new()

        exists_player_1 = pl_mapper.get('Igor')
        exists_player_1.mark_dirty()
        pl = (f'Name is {exists_player_1.name} '
              f'score is {exists_player_1.score} '
              f'level is {exists_player_1.level}.')
        print(pl)
        exists_player_1.name += ' Gamer'
        print(exists_player_1.name)

        exists_player_2 = pl_mapper.get('Fedor')
        exists_player_2.mark_removed()

        print(unitof_work.get_current().__dict__)

        unitof_work.get_current().commit()
    except Exception as e:
        print(e.args)
    finally:
        unitof_work.set_current(None)

    print(unitof_work.get_current())
    os.remove(DB_NAME)
