from pygame import image, Rect, sprite

from core.settings import configurator


class Block(sprite.Sprite):

    block_size = configurator.block_size

    def __init__(self, x, y, img):
        sprite.Sprite.__init__(self)
        self.image = image.load(f'resourses/{img}')
        self.rect = Rect(x, y, self.block_size, self.block_size)


class CreateBlock:
    _background = sprite.Group()
    _level_map = sprite.Group()
    _good_list = []

    def __init__(self):
        self._BLOCKS = {
            'M': self._lvl_block,
            '*': self._lvl_block,
            'B': self._lvl_block,
            '#': self._backg_round,
            'A': self._good_staff,
            'O': self._good_staff,
        }

    def __call__(self, block, x, y):
        self._block = self._check_block(block)
        self._x, self._y = x, y
        block = self._BLOCKS.get(self._block)
        if block():
            return True
        raise TypeError(f'Block not found {self._block}!')

    def _check_block(self, block):
        if block in self._BLOCKS.keys():
            return block
        else:
            return '#'

    def _backg_round(self):
        self._background.add(Block(self._x, self._y, 'sh_block.png'))
        return True

    def _lvl_block(self):
        if self._block == 'M':
            img = 'm_block.png'
        elif self._block == '*':
            img = 'b_block.png'
        else:
            img = 's_block.png'
        self._level_map.add(Block(self._x, self._y, img))
        return True

    def _good_staff(self):
        if self._block == 'A':
            img = 'apple.png'
        else:
            img = 'orange.png'
        self._backg_round()
        self._good_list.append((self._x, self._y, img))
        return True

    def get_groups(self):
        return (
            self._background,
            self._level_map,
            self._good_list,
        )
