from pygame import sprite, image, Rect, Surface


class Button(sprite.Sprite):
    """ Class create button use sprite image
        Arguments:
            image_file -- str, Path to image file of button
            x -- int, destanation of message, always center
            y -- int, destanation of message
    """
    _state = 0
    max_state = 3
    _width = 400
    _heigth = 100
    _btn_states = []
    _x, _y = 0, 0

    def __init__(self, image_file, x, y):
        sprite.Sprite.__init__(self)
        self._sprites = image.load(image_file)
        self._get_states()
        self.rect = Rect(0, 0, self._width, self._heigth)
        self._coords(x, y)

    def _get_states(self):
        """Create states of button from sprites image"""
        for i in range(self.max_state):
            x = -i * self._width
            rect = Rect(x, 0, self._width, self._heigth)
            _surface = Surface((self._width, self._heigth))
            _surface.blit(self._sprites, rect)
            self._btn_states.append(_surface)

    def _coords(self, x, y):
        self.rect.x, self.rect.y = x - self._width//2, y

    def check_state(self, x, y, pressed=False):
        check = (
            x > self.rect.left and
            x < self.rect.right and
            y > self.rect.top and
            y < self.rect.bottom
        )
        if check:
            self._state = 1
            if pressed:
                self._state = 0
                return True
        else:
            self._state = 0
        return False

    def render(self):
        self._btn = self._btn_states[self._state]
        return (self._btn, self.rect)
