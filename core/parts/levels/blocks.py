from pygame import image, Rect, sprite

from core.settings import configurator
from core.commons.types import TileTypes


lvl_blocks = TileTypes({
    'U': 'u_block.png',
    'B': 'b_block.png',
    '*': 's_block.png',
})

bg_blocks = TileTypes({
   '#': 'sh_block.png',
   'G': 'g_block.png',
   'T': 't_block.png',
   'F': 'f_block.png',
})


class Block(sprite.Sprite):

    block_size = configurator.block_size

    def __init__(self, x, y, img):
        sprite.Sprite.__init__(self)
        self.image = image.load(f'resourses/{img}')
        self.rect = Rect(x, y, self.block_size, self.block_size)


def create_block(blocks: list) -> sprite.Group:
    """Fabric method for Block create
        Arguments:
            blocks -- list > List of block params etc [(x, y, img), ...]
    """
    block_group = sprite.Group()
    block_list = tuple(Block(*ent) for ent in blocks)
    block_group.add(block_list)
    return block_group
