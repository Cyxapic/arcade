from .commons import miniature
from .commons import message


class EndLevel(miniature):
    """Class render and draw Game Over screenS
        Arguments:
            screen -- Main diesplay surface
            player -- player object
    """
    _score = None

    def _create_titles(self):
        x = self.width // 2
        y = 400
        title = message(x, y, '*** Это победа! ***', 45)
        text = f'*** Итого набрано: {self._score} ***'
        sub_title = message(x, y+100, text, 35)
        return title.render(), sub_title.render()

    def run(self, score):
        """Entry point method"""
        self._score = score
        self._titles = self._create_titles()
        self.screen.blits(((self._img, self._rect), *self._titles))
