import pygame

BEIGE= (210, 190, 150)
class Operations:

    def __init__(self, x, y, operation, name):
        font = pygame.font.Font('font/Pixeltype.ttf', 60)
        self.surface = font.render(operation, False, (64, 64, 64))
        self.rect = self.surface.get_rect(center=(x, y))
        self.name = name

    def draw(self,display_surface, color= BEIGE):
        pygame.draw.circle(display_surface, color, self.rect.center, 50)
        display_surface.blit(self.surface, self.rect)

class Levels:
    def __init__(self, x, y, niveau, name):
        font = pygame.font.Font('font/Pixeltype.ttf', 60)
        self.surface = font.render(name, False, (64, 64, 64))
        self.rect = self.surface.get_rect(center=(x, y))
        self.niveau = niveau
        self.name = name

    def draw(self, display_surface, color=BEIGE):
        pygame.draw.circle(display_surface, color, self.rect.center, 50)
        display_surface.blit(self.surface, self.rect)

class Display_Operation:
    def __init__(self, operation=None):
        font = pygame.font.Font('font/Pixeltype.ttf', 40)
        self.operation_surf = font.render(f'{operation}', False, (64, 64, 64))
        self.rect = self.operation_surf.get_rect(topleft=(50, 130))
        self.rect.h += 5

