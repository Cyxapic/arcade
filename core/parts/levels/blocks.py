from pygame import image, Rect, sprite

from core.settings import configurator


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
