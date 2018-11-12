from pygame import font, sprite


FONT = font.match_font('Sans')


class Message(sprite.Sprite):
    """ Create text messages on screen
        Arguments:
            x, y -- int, destanation of message
            text -- str, message text
        Keyword arguments:
            font_size -- int
    """
    _msg = None
    _rect = None

    def __init__(self, x: int, y: int, text: str, font_size=22):
        sprite.Sprite.__init__(self)
        self.font = font.Font(FONT, font_size)
        self._x = x
        self._y = y
        self.text = text
        self._render_text()
        self._get_rect()

    def _render_text(self):
        self._msg = self.font.render(self.text, 1, (255, 255, 255))

    def _get_rect(self):
        self._rect = self._msg.get_rect()
        self._rect.x, self._rect.y = self._x - self._rect.width // 2, self._y

    def update(self, text: str):
        """ Update text message method
            Arguments:
                text -- str, message text
        """
        self.text = text
        self._render_text()

    def render(self):
        return self._msg, self._rect
