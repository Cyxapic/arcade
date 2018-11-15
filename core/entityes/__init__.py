from pygame import sprite

from .enemy import Enemy
from .good_staff import GoodStaff


ENTITYES = {
            'enemy': Enemy,
            'goodstaff': GoodStaff,
        }


def create_entity(cls: str, file: str, size: tuple, quantity=None):
    """Fabric method for Entity create
        Arguments:
            cls -- str > Name of entity class
            file -- str (path to sprite file)
            size -- tuple > (screen_width, screen_heigth)
        Keyword arguments:
            quantity -- int > quantity of entityes
            if quantity returns a list of entity_object
    """
    entity = ENTITYES.get(cls)
    if not entity:
        raise AssertionError(f'Bad cls {cls}')
    if not quantity:
        return entity(file, size)
    entity_group = sprite.Group()
    entity_list = (entity(file, size) for _ in range(quantity))
    entity_group.add(entity_list)
    return entity_group
