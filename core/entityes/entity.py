from pygame import sprite, image


class Entity(sprite.Sprite):
    """ Entityes in game
        Arguments:
            file -- str (path to sprite file)
            size -- tuple (screen_width, screen_heght)
    """
    def __init__(self, x: int, y: int, file: str):
        sprite.Sprite.__init__(self)
        self._load_image(file)
        self.rect.x, self.rect.y = x, y
        self.start_x, self.start_y = x, y

    def _load_image(self, file):
        self.image = image.load(f'resourses/{file}')
        self.rect = self.image.get_rect()
