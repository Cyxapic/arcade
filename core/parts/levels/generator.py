from pygame import Surface

from core.settings import configurator

from ..commons.loader import resourses


class LevelGenerator:
    _data = None

    def __init__(self):
        self._level = configurator.get_lvl()
        self.block_size = configurator.block_size
        self.screen_size = configurator.get_screen()
        self.screen = Surface(configurator.get_screen())

    def _generate_level(self):
        x = 0
        y = 0
        for row in self._level:
            for col in row:
                res = resourses.get(col, '#')
                rect = res.get_rect()
                rect.x, rect.y = x, y
                self.screen.blit(res, rect)
                x += self.block_size[0]
            y += self.block_size[0]
            x = 0

    def get_level(self):
        self._generate_level()
        return self.screen
