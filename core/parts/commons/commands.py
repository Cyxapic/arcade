import pygame


class CommandButtons:
    def __init__(self, status):
        self.status = status

    def execute(self, event):
        return self.status


class GameStartMouseCmd(CommandButtons):
    def execute(self, event, btn):
        if not event:
            return
        coords = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            btn.check_state(*coords)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if btn.check_state(*coords, pressed=True):
                return self.status


class GoMenuCmd(CommandButtons):
    def execute(self, event):
        if not event:
            return
        if event.type == pygame.KEYDOWN \
           and pygame.key.name(event.key) == 'escape':
            return self.status


class LeaveGameCmd(CommandButtons):
    def execute(self, event):
        if not event:
            return
        if event.type == pygame.KEYDOWN \
           and pygame.key.name(event.key) == 'escape':
            if self.status == 'menu':
                exit()
