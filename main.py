import pygame

from core.game import Game
from core.settings import configurator


SIZE = configurator.get_screen()
BLACK = 0, 0, 0
sound = 'resourses/sounds/little_Hedgehog.mp3'
icon = 'resourses/icon.png'

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()

icon = pygame.image.load(icon)
pygame.display.set_icon(icon)
pygame.display.set_caption('Приключения ежика!')

screen = pygame.display.set_mode(SIZE)
game = Game(screen)

pygame.mixer.music.load(sound)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    screen.fill(BLACK)
    game.run()
    pygame.display.flip()
