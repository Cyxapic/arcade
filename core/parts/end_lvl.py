import os

from core.settings import configurator

from .commons import miniature
from .commons import message


class EndLevel(miniature):
    """Class render and draw Game Over screenS
        Arguments:
            screen -- Main diesplay surface
            player -- player object
    """
    _score = None
    end_title = 'That\' all!'

    def _create_titles(self):
        x = self.width // 2
        y = 400
        title = message(x, y, '*** Это победа! ***', 45)
        text = f'*** Итого набрано: {self._score} ***'
        sub_title = message(x, y+100, text, 35)
        end_title = message(x, y+200, self.end_title, 35)
        return title.render(), sub_title.render(), end_title.render()

    def new_level(self):
        number = configurator.get_lvl_number
        number += 1
        level_file = f'resourses/levels/level_{number}.lvl'
        if os.path.exists(level_file):
            configurator.set_lvl(number)
            self.end_title = f'Go to the next level {number}'
        return 'end_lvl'

    def run(self, score):
        """Entry point method"""
        self._score = score
        self.screen.blits(((self._img, self._rect), *self._create_titles()))
