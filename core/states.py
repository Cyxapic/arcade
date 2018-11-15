from core.parts import create_part


class GameState:
    """ Game states for Game object
        Arguments:
            screen -- Main Surface screen
            player -- Player object
    """
    def __init__(self, screen, player):
        self.screen = screen
        self._player = player
        self._create_states()

    def __call__(self):
        return {
            'menu': self._menu,
            'gen_lvl': self._gen_lvl,
            'level': self._level,
            'end_lvl': self._end_lvl,
            'gameover': self._gameover,
        }

    def _create_states(self):
        def path_(name): return f'resourses/{name}'
        self.menu_part = create_part('menu', self.screen, path_('menu.png'))
        self.level_part = create_part('level', self.screen, self._player)
        self.end_lvl_part = create_part('end_lvl', self.screen, path_('win.png'))
        self.gameover_part = create_part('gameover', self.screen, path_('gameover.png'))

    def _menu(self):
        return self.menu_part.run()

    def _gen_lvl(self):
        return self.level_part.start_level()

    def _level(self):
        return self.level_part.run()

    def _end_lvl(self):
        return self.end_lvl_part.run(self._player.get_score)

    def _gameover(self):
        return self.gameover_part.run()
