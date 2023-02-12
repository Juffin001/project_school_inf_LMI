import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

    def collide_point(self, x, y):
        return self.rect.collidepoint(x, y)
