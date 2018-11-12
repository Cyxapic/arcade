from random import randint

import pygame

from core.entityes import create_entity
from .messages import Message


class GameLevel:
    """ Create level
        Arguments:
            screen -- Main diesplay surface
            player -- Player object
    """
    fruit_quantity = 0
    enemy_quantity = 0
    background = pygame.image.load('resourses/background.png')
    background_rect = background.get_rect()

    def __init__(self, screen, player):
        self.screen = screen
        self._get_screen()
        self.player = player

    def _get_screen(self):
        width, height = self.screen.get_size()
        self.game_screen = pygame.Surface((width, height-100))
        self.game_rect = self.game_screen.get_rect()
        self.game_rect.y = 100
        self.size = self.game_screen.get_size()

    def _level_init(self):
        """start new stage"""
        self.player.reset()
        self.msg_scores = Message(100, 20, f'Очки: 0', 35)
        self.msg_lives = Message(300, 20, f'Жизни: 3', 35)
        self.enemy_quantity = randint(5, 20)
        self.fruit_quantity = randint(5, 20)
        # generate entityes
        self.shit_list = create_entity('enemy', self.size, self.enemy_quantity)
        self.fruits_list = create_entity('goodstaff', self.size, self.fruit_quantity)
        # DEBUG OUTPUT QUANTITY OF FRUIT***********************************************
        self._fruit_quantity = Message(550, 20, f'Всего фруктов: {self.fruit_quantity}', 35)
        # *****************************************************************************

    def _render_entity(self, *entity_lists):
        for entity_list in entity_lists:
            self.game_screen.blits((entity.render() for entity in entity_list))

    def start_level(self):
        self._level_init()
        return 'level'

    def run(self):
        pressed = pygame.key.get_pressed()
        self.player.move(pressed)
        self.player.check_boundaries(self.size)
        shit_hit_list = pygame.sprite.spritecollide(self.player, self.shit_list, True)
        if shit_hit_list:
            if self.player.shiteater:
                return 'gameover'
            self.player.crash()
            self.msg_lives.update(f'Жизни: {self.player.get_lives}')
        good_hit_list = pygame.sprite.spritecollide(self.player, self.fruits_list, True)
        if good_hit_list:
            self.player.eat_fruit()
            self.msg_scores.update(f'Очки: {self.player.get_score}')
        if self.player.get_score == self.fruit_quantity:
            return 'end_lvl'
        labels = (
                self.msg_scores.render(),
                self.msg_lives.render(),
                self._fruit_quantity.render()
            )
        # RENDER!
        self.game_screen.blit(self.background, self.background_rect)
        self._render_entity(self.shit_list, self.fruits_list)
        self.game_screen.blit(*self.player.render())
        self.screen.blits(labels)
        self.screen.blit(self.game_screen, self.game_rect)
