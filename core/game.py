import pygame

from core import parts
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
    state = 'menu'
    player = Player('resourses/hedgehoc.png')

    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.STATES = self._get_states()

    def _get_states(self):
        def path_(name): return f'resourses/{name}'
        menu = parts.Menu(self.screen, path_('menu.png'))
        level = parts.GameLevel(self.screen, self.player)
        end_lvl = parts.EndLevel(self.screen, path_('win.png'), player=self.player)
        gameover = parts.GameOver(self.screen, path_('gameover.png'))
        return {
            'menu': menu.run,
            'gen_lvl': level.start_level,
            'level': level.run,
            'end_lvl': end_lvl.run,
            'gameover': gameover.run,
        }

    def _events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if self.state == 'menu':
                    if pygame.key.name(event.key) == 'escape':
                        exit()
                if self.state in ('end_lvl', 'gameover', 'level'):
                    if pygame.key.name(event.key) == 'escape':
                        self.state = 'menu'

    def run(self, pressed):
        """ Entry point of Game"""
        self._events()
        state = self.STATES.get(self.state)()
        if state:
            self.state = state
            state = None
