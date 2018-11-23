from random import randint

import pygame

from core.settings import configurator

from core.entityes import create_entity
from core.parts.commons import message

from .generator import LevelGenerator


class GameLevel:
    """ Create level
        Arguments:
            screen -- Main diesplay surface
            player -- Player object
    """
    fruit_quantity = 0
    enemy_quantity = 0

    def __init__(self, screen, player):
        self.screen = screen
        self._get_screen()
        self.player = player
        self.level_gen = LevelGenerator()
        self.block_size = configurator.block_size
        self.game_screen = pygame.Surface(configurator.get_screen())

    def _get_screen(self):
        width, height = self.screen.get_size()
        self.size = (100, 900) # self.game_screen.get_size()

    def _level_init(self):
        """start new stage"""
        self.player.reset()
        self.msg_scores = message(100, 65, f'Очки: 0', 25)
        self.msg_lives = message(300, 65, f'Жизни: 3', 25)
        self.enemy_quantity = randint(5, 20)
        self.fruit_quantity = randint(5, 20)
        # generate entityes
        self.shit_list = create_entity(
            'enemy',
            'kakashka.png',
            self.size,
            quantity=self.enemy_quantity
        )
        self.fruits_list = create_entity(
            'goodstaff',
            'good_staff.png',
            self.size,
            quantity=self.fruit_quantity
        )
        # DEBUG OUTPUT QUANTITY OF FRUIT***********************************************
        self._fruit_quantity = message(550, 65, f'Всего фруктов: {self.fruit_quantity}', 25)
        # *****************************************************************************

    def _render(self):
        # !!!!!!!!!!! НЕ РАБОТАЕТ!!!!!!!!!!
        # ЧТО ТО С КООРДИНАТАМИ!!!!!!!!!!!!
        self.game_screen.fill((0,0,0))
        # self.game_screen.blits(((block.image, block.rect) for s in self.level_gen.all_map))
        for block in self.level_gen.all_map:
            # self.game_screen.blit(block.image, block.rect)
            self.game_screen.blit(block.image, pygame.Rect(randint(100, 900), randint(100, 900), 32, 32))

    def _render_entity(self, *entity_lists):
        for entity_list in entity_lists:
            self.game_screen.blits((entity.render() for entity in entity_list))

    def start_level(self):
        self._level_init()
        return 'level'

    def run(self):
        pressed = pygame.key.get_pressed()
        self.player.move(pressed)
        # self.player.check_boundaries(self.size)
        self.player.collide(self.level_gen.platforms)
        # shit_hit_list = pygame.sprite.spritecollide(self.player, self.shit_list, True)
        # if shit_hit_list:
        #     if self.player.shiteater:
        #         return 'gameover'
        #     self.player.crash()
        #     self.msg_lives.update(f'Жизни: {self.player.get_lives}')
        # good_hit_list = pygame.sprite.spritecollide(self.player, self.fruits_list, True)
        # if good_hit_list:
        #     self.player.eat_fruit()
        #     self.msg_scores.update(f'Очки: {self.player.get_score}')
        # if self.player.get_score == self.fruit_quantity:
        #     return 'end_lvl'
        labels = (
                self.msg_scores.render(),
                self.msg_lives.render(),
                self._fruit_quantity.render()
            )
        # RENDER!
        self._render()
        self.game_screen.blits(labels)
        self.game_screen.blit(*self.player.render())
        # self.screen.blit(self.level, self.level.get_rect())
        
        # self._render_entity(self.shit_list, self.fruits_list)
        
        self.screen.blit(self.game_screen, self.game_screen.get_rect())
