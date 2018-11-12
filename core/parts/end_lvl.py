from .miniature import Miniature
from .messages import Message


class EndLevel(Miniature):
    """Class render and draw Game Over screenS
        Arguments:
            screen -- Main diesplay surface
            player -- player object
    """
    _score = None

    def __init__(self, *args, **kwargs):
        self._player = kwargs.pop('player')
        super().__init__(*args)

    def _create_titles(self):
        x = self.width // 2
        y = 400
        title = Message(x, y, '*** Это победа! ***', 45)
        text = f'*** Итого набрано: {self._score} ***'
        sub_title = Message(x, y+100, text, 35)
        return title.render(), sub_title.render()

    def run(self):
        """Entry point method"""
        self._score = self._player.get_score
        self._titles = self._create_titles()
        self.screen.blits(((self._img, self._rect), *self._titles))
