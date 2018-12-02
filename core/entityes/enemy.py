from random import choice

from .entity import Entity


class Enemy(Entity):
    """ create an enemy """
    start = 0
    direction = 1
    change_dir = True

    def _animate(self):
        """Moves Entity foward and backward"""
        steps = (1, 7, 14)
        if self.rect.x < self.start_x - 100:
            self.change_dir = False
        elif self.rect.x > self.start_x + 100:
            self.change_dir = True
        self.direction = -1 if self.change_dir else 1
        self.rect.x += self.direction * choice(steps)

    def render(self, blocks):
        for block in blocks:
            if self.collide_rect(self, block):
                self.change_dir = True

        self._animate()
        return (self.image, self.rect)
