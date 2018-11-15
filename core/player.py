import pygame


pygame.mixer.init()


class Player:
    """ Create player object
        Arguments:
            imgfile -- path to imagefile (sprites)
    """
    _score = 0
    _lives = 3
    x = 0
    frames = []
    max_frames = 4
    current_frame = 0
    speed = 10

    def __init__(self, imgfile: str):
        self._player_sprite = pygame.image.load(imgfile)
        self.rect = self._get_rect()
        self._get_frames()
        self._player = self.frames[self.current_frame]
        self._player.set_colorkey((0, 255, 0))
        self._sound_init()

    def _get_rect(self):
        return pygame.Rect(0, 0, 60, 80)

    def _get_frames(self):
        """Create frames from sprites image"""
        for i in range(self.max_frames):
            x = -i * 60
            rect = pygame.Rect(x, 0, 60, 80)
            player_surface = pygame.Surface((60, 80))
            player_surface.blit(self._player_sprite, rect)
            self.frames.append(player_surface)

    def _sound_init(self):
        crash_snd_file = 'resourses/puk.ogg'
        fruit_yaaa_file = 'resourses/eat.ogg'
        self.crash_snd = pygame.mixer.Sound(crash_snd_file)
        self.fruit_yaaa = pygame.mixer.Sound(fruit_yaaa_file)

    def crash(self):
        self._lives -= 1
        self.crash_snd.play()
        self.current_frame += 1
        self._player = self.frames[self.current_frame]
        self._player.set_colorkey((0, 255, 0))

    def move(self, pressed: tuple):
        KEYS = {
            pygame.K_LEFT: (-self.speed, 0),
            pygame.K_RIGHT: (self.speed, 0),
            pygame.K_DOWN: (0, self.speed),
            pygame.K_UP: (0, -self.speed),
        }
        speed = [val for key, val in KEYS.items() if pressed[key]]
        if speed:
            self.rect = self.rect.move(speed[0])

    @property
    def shiteater(self):
        return True if self._lives == 0 else False

    @property
    def get_score(self):
        return self._score

    @property
    def get_lives(self):
        return self._lives

    def eat_fruit(self):
        self._score += 1
        self.fruit_yaaa.play()

    def render(self):
        return (self._player, self.rect)

    def check_boundaries(self, size: tuple):
        width, height = size
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height

    def reset(self):
        self._score = 0
        self._lives = 3
        self.current_frame = 0
        self._player = self.frames[self.current_frame]
        self.rect.x = 0
        self.rect.y = 0
