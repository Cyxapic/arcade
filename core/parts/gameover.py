from .miniature import Miniature
from .messages import Message


class GameOver(Miniature):
    """Class render and draw Game Over screenS
        Arguments:
            screen -- Main diesplay surface
    """
    def _create_titles(self):
        x = self.width // 2
        y = 400
        title = Message(x, y, '*** ФУУУУУУУ ***', 45)
        sub_title = Message(x, y+100, f'*** Весь в какашках!!! ***', 35)
        return title.render(), sub_title.render()
