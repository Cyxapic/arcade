from random import choice
from pygame import image, Rect, Surface

from .entity import Entity


class GoodStaff(Entity):
    """ Create good staff - fruits
        whith random sprite images
    """
    max_staff = 3
    staff_size = (60, 60)

    def _load_image(self, file):
        self.image = image.load(f'resourses/{file}')
        self.image = choice(self._get_staff())
        self.image.set_colorkey((0, 255, 0))
        self.rect = self.image.get_rect()

    def _get_staff(self):
        """Create frames from sprites image"""
        staff_list = []
        for i in range(self.max_staff):
            x = -i * self.staff_size[0]
            rect = Rect(x, 0, *self.staff_size)
            staff = Surface(self.staff_size)
            staff.blit(self.image, rect)
            staff_list.append(staff)
        return staff_list
