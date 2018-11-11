from random import randint, choice

from pygame import sprite, image


class Entity(sprite.Sprite):
    """ Entityes in game
        Arguments:
            size -- tuple(screen_width, screen_heght)
    """
    file = None

    def __init__(self, size: tuple):
        sprite.Sprite.__init__(self)
        self.size = size
        self._load_image()
        self._coords()

    def _load_image(self):
        self.image = image.load(self.file)
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

    # @staticmethod
    # def create_entity(cls: str, size: tuple, quantity=None):
    #     """Fabric method for Entity create
    #         Arguments:
    #             cls -- str > Name of entity class
    #             size -- tuple > (screen_width, screen_heigth)
    #         Keyword arguments:
    #             quantity -- int > quantity of entityes
    #             if quantity returns a list of entity_object
    #     """
    #     entityes = {
    #         'enemy': Enemy,
    #         'goodstaff': GoodStaff,
    #     }
    #     entity = entityes.get(cls)
    #     if not entity:
    #         raise AssertionError(f'Bad cls {cls}')
    #     if not quantity:
    #         return entity(size)
    #     entity_group = sprite.Group()
    #     entity_list = (entity(size) for _ in range(quantity))
    #     entity_group.add(entity_list)
    #     return entity_group
