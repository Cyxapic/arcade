from core.settings import configurator

from ..commons.loader import resourses


class LevelGenerator:
    _data = None
    all_map = []
    platforms = []

    def __init__(self):
        self._level = configurator.get_lvl()
        self.block_size = configurator.block_size
        self.res = resourses
        self._generate_level()

    def _generate_level(self):
        x = 0
        y = 0
        for row in self._level:
            for col in row:
                res1 = self.res.get(col)
                res = res1 if res1 else self.res.get('#')
                res.rect.x, res.rect.y = x, y
                if res1:
                    self.platforms.append(res)
                self.all_map.append(res)
                x += self.block_size[0]
            y += self.block_size[0]
            x = 0
