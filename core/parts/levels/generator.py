from core.settings import configurator
from core.entityes import goodstaff, enemy
from .blocks import lvl_blocks, bg_blocks


class LevelCreator:
    """ Create and return tuple of list > Blocks params """
    _block_size = configurator.block_size

    def __init__(self):
        self._BLOCKS = {
            lvl_blocks.get_types: self._lvl_block,
            goodstaff.get_types: self._good_staff,
            enemy.get_types: self._enemies,
            bg_blocks.get_types: self._backg_round,
        }
        self._background = []
        self._level_map = []
        self._good_list = []
        self._enemy_list = []
        self._calc()

    def _add_block(self,  block, x, y):
        self._block = block
        self._x, self._y = x, y
        for bl, func in self._BLOCKS.items():
            if self._block in bl:
                return func()
        raise TypeError(f'Block not found {self._block}!')

    def _calc(self):
        x = 0
        y = 0
        _level = configurator.get_lvl()
        for row in _level:
            for col in row:
                if col == chr(10):
                    continue
                if not self._add_block(col, x, y):
                    raise AttributeError('Error creating blog!')
                x += self._block_size
            y += self._block_size
            x = 0

    def _backg_round(self):
        images = bg_blocks.get_types_img
        image = images.get(self._block)
        image = image if image else images.get('#')
        self._background.append((self._x, self._y, image))
        return True

    def _lvl_block(self):
        images = lvl_blocks.get_types_img
        self._level_map.append((self._x, self._y, images[self._block]))
        return True

    def _good_staff(self):
        images = goodstaff.get_types_img
        self._backg_round()
        self._good_list.append((self._x, self._y, images[self._block]))
        return True

    def _enemies(self):
        images = enemy.get_types_img
        self._backg_round()
        self._enemy_list.append((self._x, self._y, images[self._block]))
        return True

    def get_groups(self):
        return (
            self._background,
            self._level_map,
            self._good_list,
            self._enemy_list,
        )
