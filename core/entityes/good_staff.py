from random import choice
from pygame import image

from .entity import Entity


class GoodStaff(Entity):
    """ Create good staff - fruits
        whith random sprite images
    """
    file = (
                'resourses/apple.png',
                'resourses/apple1.png',
                'resourses/orange.png',
            )

    def _load_image(self):
        img = choice(self.file)
        self.image = image.load(img)
        self.rect = self.image.get_rect()
