from abc import ABC, abstractmethod
from pygame import image


class Miniature(ABC):
    """ Parent class for menu, gameover etc
        Arguments:
            screen -- Main display surface
            image_file -- image file path
    """
    def __init__(self, screen, image_file):
        self.screen = screen
        self.width, self.heigth = screen.get_size()
        self._img = image.load(image_file)
        self._get_rect()

    def _get_rect(self):
        self._rect = self._img.get_rect()
        self._rect.x = self.width // 2 - self._rect.width // 2
        self._rect.y = 50

    @abstractmethod
    def _create_titles(self):
        """ Render titles method
            must return tuple
            ((Surface, dest), ... )
        """

    def run(self):
        """Entry point method"""
        self.screen.blits(((self._img, self._rect), *self._create_titles()))
