from core.parts import create_part
from core.parts.commons import (go_menu_cmd,
                                leave_game_cmd,
                                game_start_cmd)

from .player import Player


class GameState:
    """ Game states for Game object
        Arguments:
            screen -- Main Surface screen
            player -- Player object
    """
    event = None
    _player = Player('resourses/hedgehoc.png')

    def __init__(self, screen):
        self.screen = screen
        self.states = self._create_states()

    def __call__(self, state):
        if state:
            return self.states[state]

    def _create_states(self):
        def path_(name): return f'resourses/{name}'
        self.menu_part = create_part('menu', self.screen, path_('menu.png'))
        self.level_part = create_part('level', self.screen, self._player)
        self.end_lvl_part = create_part('end_lvl', self.screen, path_('win.png'))
        self.gameover_part = create_part('gameover', self.screen, path_('gameover.png'))
        return {
            'menu': self._menu,
            'gen_lvl': self._gen_lvl,
            'level': self._level,
            'new_lvl': self._new_lvl,
            'end_lvl': self._end_lvl,
            'gameover': self._gameover,
        }

    def _menu(self):
        leave_game_cmd.execute(self.event)
        self.menu_part.run()
        return game_start_cmd.execute(self.event, self.menu_part.start_btn)

    def _gen_lvl(self):
        return self.level_part.start_level()

    def _level(self):
        menu = go_menu_cmd.execute(self.event)
        self._player.get_event(self.event)
        self.event = None
        return menu if menu else self.level_part.run()

    def _new_lvl(self):
        return self.end_lvl_part.new_level()

    def _end_lvl(self):
        menu = go_menu_cmd.execute(self.event)
        self.event = None
        return menu if menu else self.end_lvl_part.run(self._player.get_score)

    def _gameover(self):
        menu = go_menu_cmd.execute(self.event)
        self.event = None
        return menu if menu else self.gameover_part.run()

    def get_start(self):
        return 'menu'

    def get_event(self, event):
        """ event - pygame.event object """
        self.event = event
