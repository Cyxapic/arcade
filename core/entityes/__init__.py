from pygame import sprite

from core.commons.types import TileTypes

from .enemy import Enemy
from .good_staff import GoodStaff


ENTITYES = {
            'enemy': Enemy,
            'goodstaff': GoodStaff,
        }

goodstaff = TileTypes({
        'A': 'apple.png',
        'O': 'mushroom.png',
    })

enemy = TileTypes({
        'S': 'kakashka.png',
        'R': 'robot.png',
    })


def create_entity(cls: str, entity_args: list) -> sprite.Group:
    """Fabric method for Entity create
        Arguments:
            cls -- Entitty class
            entity_args -- list > List of entity params etc [(x, y, img), ...]
    """
    entity = ENTITYES.get(cls)
    if not entity:
        raise AssertionError(f'Wrong entity class!')
    entity_group = sprite.Group()
    entity_list = tuple(entity(*ent) for ent in entity_args)
    entity_group.add(entity_list)
    return entity_group
