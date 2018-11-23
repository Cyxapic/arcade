from .levels import gamelevel
from .menu import Menu
from .end_lvl import EndLevel
from .gameover import GameOver


def create_part(part_name, screen, *args, **kwargs):
    PARTS = {
            'menu': Menu,
            'level': gamelevel,
            'end_lvl': EndLevel,
            'gameover': GameOver,
        }
    part_cls = PARTS.get(part_name)
    if not part_cls:
        raise TypeError('Part not found!')
    return part_cls(screen, *args, **kwargs)
