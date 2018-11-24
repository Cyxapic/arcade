from core.settings import configurator


class LevelCreator:
    """ Create and return tuple of list > Blocks params """
    _block_size = configurator.block_size

    def __init__(self):
        self._BLOCKS = {
            ('M', 'B', '*'): self._lvl_block,
            ('A', 'O'): self._good_staff,
            ('#', ): self._backg_round,
        }
        self._background = []
        self._level_map = []
        self._good_list = []
        self._calc()

    def _add_block(self,  block, x, y):
        self._block = '#' if block == chr(32) else block
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
        self._background.append((self._x, self._y, 'sh_block.png'))
        return True

    def _lvl_block(self):
        images = {
            'M': 'm_block.png',
            'B': 'b_block.png',
            '*': 's_block.png',
        }
        self._level_map.append((self._x, self._y, images[self._block]))
        return True

    def _good_staff(self):
        images = {
            'A': 'apple.png',
            'O': 'orange.png',
        }
        self._backg_round()
        self._good_list.append((self._x, self._y, images[self._block]))
        return True

    def _enemies(self):
        pass

    def get_groups(self):
        return (
            self._background,
            self._level_map,
            self._good_list,
        )
