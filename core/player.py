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
    LEFT = False
    RIGHT = False
    DOWN = False
    UP = False

    def __init__(self, imgfile: str):
        self._player_sprite = pygame.image.load(imgfile)
        self.rect = self._get_rect()
        self._get_frames()
        self._player = self.frames[self.current_frame]
        self._player.set_colorkey((0, 255, 0))
        self._sound_init()

    def _get_rect(self):
        return pygame.Rect(100, 260, 45, 60)

    def _get_frames(self):
        """Create frames from sprites image"""
        for i in range(self.max_frames):
            x = -i * 45
            rect = pygame.Rect(x, 0, 45, 60)
            player_surface = pygame.Surface((45, 60))
            player_surface.blit(self._player_sprite, rect)
            self.frames.append(player_surface)

    def _sound_init(self):
        crash_snd_file = 'resourses/sounds/puk.ogg'
        fruit_yaaa_file = 'resourses/sounds/eat.ogg'
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
            pygame.K_LEFT: 'LEFT',
            pygame.K_RIGHT: 'RIGHT',
            pygame.K_DOWN: 'DOWN',
            pygame.K_UP: 'UP',
        }
        direction = [val for key, val in KEYS.items() if pressed[key]]
        direction = direction[0] if direction else None
        if direction == 'LEFT':
            move = (-self.speed, 0)
            self.LEFT = True
        elif direction == 'RIGHT':
            self.RIGHT = True
            move = (self.speed, 0)
        elif direction == 'DOWN':
            move = (0, self.speed)
            self.DOWN = True
        elif direction == 'UP':
            move = (0, -self.speed)
            self.UP = True
        else:
            move = None
            self.LEFT = False
            self.RIGHT = False
            self.DOWN = False
            self.UP = False
        if move:
            self.rect = self.rect.move(move)

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

    def collide(self, blocks):
        for block in blocks:
            if pygame.sprite.collide_rect(self, block):
                if self.rect.bottom > block.rect.top and self.DOWN:
                    self.rect.bottom = block.rect.top
                elif self.rect.top < block.rect.bottom and self.UP:
                    self.rect.top = block.rect.bottom
                elif self.rect.left < block.rect.right and self.LEFT:
                    self.rect.left = block.rect.right
                elif self.rect.right > block.rect.left and self.RIGHT:
                    self.rect.right = block.rect.left

    def reset(self):
        self._score = 0
        self._lives = 3
        self.current_frame = 0
        self._player = self.frames[self.current_frame]
        self.rect.x = 100
        self.rect.y = 260
