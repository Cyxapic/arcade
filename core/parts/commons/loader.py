from pygame import image, Rect, Surface

from core.settings import configurator


def resourse_loader():
    block_size = configurator.block_size
    sprites = image.load('resourses/blocks.png')
    blocks = ('M', '*', 'B', '#', )
    BLOCKS = {}
    xi = 0
    for block in blocks:
        x = -xi * block_size[0]
        rect = Rect(x, 0, *block_size)
        staff = Surface(block_size)
        staff.blit(sprites, rect)
        BLOCKS[block] = staff
        xi += 1

    return BLOCKS


resourses = resourse_loader()
