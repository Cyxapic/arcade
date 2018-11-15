from .commons import miniature
from .commons import message


class GameOver(miniature):
    """Class render and draw Game Over screenS
        Arguments:
            screen -- Main diesplay surface
    """
    def _create_titles(self):
        x = self.width // 2
        y = 400
        title = message(x, y, '*** ФУУУУУУУ ***', 45)
        sub_title = message(x, y+100, f'*** Весь в какашках!!! ***', 35)
        return title.render(), sub_title.render()
