from random import randint

import pygame

from core.settings import configurator

from core.entityes import create_entity
from core.parts.commons import message

from .loader import CreateBlock


class GameLevel:
    """ Create level
        Arguments:
            screen -- Main diesplay surface
            player -- Player object
    """
    fruit_quantity = 0
    enemy_quantity = 0
    create_block = CreateBlock()
    _level_groups = None

    def __init__(self, screen, player):
        self.screen = screen
        self._get_screen()
        self.player = player
        self._level = configurator.get_lvl()
        self.block_size = configurator.block_size
        self.game_screen = pygame.Surface(configurator.get_screen())

    def _get_screen(self):
        width, height = self.screen.get_size()
        self.size = (100, 900) # self.game_screen.get_size()

    def _level_init(self):
        """start new stage"""
        self._render()
        self.player.reset()
        self.msg_scores = message(100, 65, f'Очки: {self.player.get_score}', 25)
        self.msg_lives = message(300, 65, f'Жизни: 3', 25)
        # generate entityes
        self.fruits_list = create_entity('goodstaff', self._good_staff)
        # self.enemy_quantity = randint(5, 20)
        # self.fruit_quantity = randint(5, 20)
        # generate entityes
        # self.shit_list = create_entity(
        #     'enemy',
        #     'kakashka.png',
        #     self.size,
        #     quantity=self.enemy_quantity
        # )
        # self.fruits_list = create_entity(
        #     'goodstaff',
        #     'good_staff.png',
        #     self.size,
        #     quantity=self.fruit_quantity
        # )
        # # DEBUG OUTPUT QUANTITY OF FRUIT***********************************************
        # self._fruit_quantity = message(550, 65, f'Всего фруктов: {self.fruit_quantity}', 25)
        # # *****************************************************************************

    def _render(self):
        x = 0
        y = 0
        for row in self._level:
            for col in row:
                self.create_block(col, x, y)
                x += self.block_size
            y += self.block_size
            x = 0
        self._background, self._level_map, self._good_staff = self.create_block.get_groups()

    def _draw_screen(self):
        for group in (self._background, self._level_map, self.fruits_list):
            group.draw(self.game_screen)

    def start_level(self):
        self._level_init()
        return 'level'

    def run(self):
        pressed = pygame.key.get_pressed()
        self.player.move(pressed)
        self.player.collide(self._level_map)
        _good_hit = pygame.sprite.spritecollide(self.player,
                                                self.fruits_list,
                                                True)
        if _good_hit:
            self.player.eat_fruit()
        labels = (
                self.msg_scores.render(),
                self.msg_lives.render(),
                # self._fruit_quantity.render()
            )
        # RENDER!
        self._draw_screen()
        self.game_screen.blits(labels)
        self.game_screen.blit(*self.player.render())
        # On main screen
        self.screen.blit(self.game_screen, self.game_screen.get_rect())
