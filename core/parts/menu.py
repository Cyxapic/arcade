from pygame import mouse

from .commons import miniature
from .commons import message
from .commons import button


class Menu(miniature):
    """Class render and draw menu
        Arguments:
            screen -- Main diesplay surface
    """
    def __init__(self, *args):
        super().__init__(*args)
        self.start_btn = self._button()

    def _create_titles(self):
        x = self.width // 2
        y = 400
        title = message(x, y, '*** МЕНЮ ***', 45)
        return (title.render(), )

    def _button(self):
        return button('resourses/start_btn.png', self.width // 2, 500)

    @property
    def _btn_pressed(self):
        MOUSE_BTN = mouse.get_pressed()[0]
        pressed = True if MOUSE_BTN else False
        coords = mouse.get_pos()
        return self.start_btn.check_state(*coords, pressed)

    def run(self):
        """Entry point"""
        super().run()
        self.screen.blit(*self.start_btn.render())
        if self._btn_pressed:
            return 'gen_lvl'
