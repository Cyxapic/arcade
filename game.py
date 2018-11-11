import pygame

from core.game import Game


pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()

SIZE = width, height = 1200, 900
BLACK = 0, 0, 0

screen = pygame.display.set_mode(SIZE)
game = Game(screen)
icon = pygame.image.load('resourses/icon.png')

sound = 'resourses/little_Hedgehog.mp3'
pygame.mixer.music.load(sound)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

while True:
    pressed = pygame.key.get_pressed()
    screen.fill(BLACK)
    game.run(pressed)
    pygame.display.set_caption('Приключения ежика!')
    pygame.display.set_icon(icon)
    pygame.display.flip()
