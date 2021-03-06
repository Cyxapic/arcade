import pygame

from .states import GameState
from .player import Player


class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class Game(metaclass=Singleton):
    """ Main class entry poin to app
        Arguments:
            screen -- Main Surface screen
    """
    player = Player('resourses/hedgehoc.png')

    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.game_states = GameState(self.screen, self.player)
        self.state = self.game_states.get_start()
        self.STATES = self.game_states()

    def _events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                self.game_states.get_event(event)

    def run(self):
        """ Entry point of Game"""
        self._events()
        state = self.STATES.get(self.state)()
        if state:
            self.state = state
            state = None
