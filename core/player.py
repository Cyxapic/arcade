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
    _event = None
    _move = False
    _direction = None

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

    def get_event(self, event):
        self._event = event

    def move(self, pressed: tuple):
        KEYS_ = {
            'left': (-self.speed, 0),
            'right': (self.speed, 0),
            'down': (0, self.speed),
            'up': (0, -self.speed),
        }
        if self._event:
            if self._event.type == pygame.KEYDOWN:
                self._direction = pygame.key.name(self._event.key)
                if self._direction in KEYS_.keys():
                    self._move = True
            if self._event.type == pygame.KEYUP:
                self._move = False
                self._direction = None
        if self._move:
            self.rect = self.rect.move(*KEYS_[self._direction])

    def collide(self, blocks):
        # 'left': (-self.speed, 0),
        # 'right': (self.speed, 0),
        # 'down': (0, self.speed),
        # 'up': (0, -self.speed),
        for block in blocks:
            if pygame.sprite.collide_rect(self, block) and self._move:
                if self.rect.left < block.rect.right \
                    and self._direction == 'left':
                    print('left')
                    self.rect = self.rect.move(self.speed, 0)
                    self._move = False
                    break
                    # self.rect.left = block.rect.right
                    
                elif self.rect.right > block.rect.left \
                        and self._direction == 'right':
                    print('right')
                    # self.rect = self.rect.move(-self.speed, 0)
                    self.rect.right = block.rect.left
                    self._move = False
                    break
                elif self.rect.bottom > block.rect.top \
                        and self._direction == 'bottom':
                    print('bottom')
                    print(self._direction)
                    # self.rect = self.rect.move(0, -self.speed)
                    self.rect.bottom = block.rect.top
                    self._move = False
                    break
                    # self._move = False
                elif self.rect.top < block.rect.bottom \
                        and self._direction == 'top':
                    print('top')
                    # self.rect = self.rect.move(0, self.speed)
                    # self.rect.top = block.rect.bottom
                    self._move = False
                    break

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

    def reset(self):
        self._score = 0
        self._lives = 3
        self.current_frame = 0
        self._player = self.frames[self.current_frame]
        self.rect.x = 100
        self.rect.y = 260
