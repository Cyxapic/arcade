from pygame import image, Rect, sprite

from core.settings import configurator


class MBlock(sprite.Sprite):

    block_size = configurator.block_size

    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load('resourses/m_block.png')
        self.rect = Rect(0, 0, *self.block_size)


class StarBlock(sprite.Sprite):

    block_size = configurator.block_size

    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load('resourses/s_block.png')
        self.rect = Rect(0, 0, *self.block_size)


class BBlock(sprite.Sprite):

    block_size = configurator.block_size

    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load('resourses/b_block.png')
        self.rect = Rect(0, 0, *self.block_size)


class SharpBlock(sprite.Sprite):

    block_size = configurator.block_size

    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load('resourses/sh_block.png')
        self.rect = Rect(0, 0, *self.block_size)


resourses = {
        'M': MBlock(),
        '*': StarBlock(),
        'B': BBlock(),
        '#': SharpBlock(), 
    }
