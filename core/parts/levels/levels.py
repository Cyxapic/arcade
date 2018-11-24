import pygame

from core.settings import configurator
from core.entityes import create_entity
from core.parts.commons import message

from .generator import LevelCreator
from .blocks import create_block


class GameLevel:
    """ Create level
        Arguments:
            screen -- Main diesplay surface
            player -- Player object
    """
    fruit_quantity = 10
    enemy_quantity = 0
    _level_groups = None

    def __init__(self, screen, player):
        self.screen = screen
        self.player = player
        self.block_size = configurator.block_size
        self.game_screen = pygame.Surface(configurator.get_screen())

    def _level_init(self):
        """start new stage"""
        level = LevelCreator()
        self._bground, self._lvl_map, self._staff = level.get_groups()
        self.player.reset()
        self.msg_scores = message(100, 65, f'Очки: {self.player.get_score}', 25)
        self.msg_lives = message(300, 65, f'Жизни: {self.player.get_lives}', 25)
        # create blocks
        self._blocks = create_block(self._lvl_map)
        self._bg = create_block(self._bground)
        # generate entityes
        self.fruits_list = create_entity('goodstaff', self._staff)
        self.fruit_quantity = len(self.fruits_list)
        # # DEBUG OUTPUT QUANTITY OF FRUIT***********************************************
        self._fruit_quantity = message(550, 65, f'Всего фруктов: {self.fruit_quantity}', 25)
        # # *****************************************************************************

    def _draw_screen(self):
        for group in (self._bg, self._blocks, self.fruits_list):
            group.draw(self.game_screen)

    def start_level(self):
        self._level_init()
        return 'level'

    def run(self):
        pressed = pygame.key.get_pressed()
        self.player.move(pressed)
        self.player.collide(self._blocks)
        _good_hit = pygame.sprite.spritecollide(self.player,
                                                self.fruits_list,
                                                True)
        if _good_hit:
            self.player.eat_fruit()
            self.msg_scores.update(f'Очки: {self.player.get_score}')

        if self.player.get_score == self.fruit_quantity:
            return 'new_lvl'

        labels = (
                self.msg_scores.render(),
                self.msg_lives.render(),
                self._fruit_quantity.render()
            )
        # RENDER!
        self._draw_screen()
        self.game_screen.blits(labels)
        self.game_screen.blit(*self.player.render())
        # On main screen
        self.screen.blit(self.game_screen, self.game_screen.get_rect())
