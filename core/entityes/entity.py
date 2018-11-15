from random import randint

from pygame import sprite, image


class Entity(sprite.Sprite):
    """ Entityes in game
        Arguments:
            file -- str (path to sprite file)
            size -- tuple (screen_width, screen_heght)
    """
    def __init__(self, file: str, size: tuple):
        sprite.Sprite.__init__(self)
        self.size = size
        self._load_image(file)
        self._coords()

    def _load_image(self, file):
        self.image = image.load(f'resourses/{file}')
        self.rect = self.image.get_rect()

    def _coords(self):
        """Generate coords for entity(image)"""
        width, height = self.size
        self.rect.x = randint(0, (width - self.rect.width))
        self.rect.y = randint(0, (height - self.rect.height))
        self.start_x = self.rect.x
        self.start_y = self.rect.y

    def render(self):
        """ Render Entity to game size as tuple"""
        return (self.image, self.rect)
