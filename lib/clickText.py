
import pygame
from calculations import *

aqua = (25,217,255)

class clickText(pygame.sprite.Sprite):
    def __init__(self, num, size, color, x, y):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.iteration = 0
        self.opacity = 255
        self.font = pygame.font.SysFont("Arial", size)
        self.Surface = self.font.render("+" + convertDecimal(num), 1, color, None)
        W = self.Surface.get_width()
        H = self.Surface.get_height()
        self.rect = self.Surface.get_rect(center=(x, y))
        self.image = pygame.Surface((W, H))
        self.image.fill(aqua)
        self.image.blit(self.Surface, (0, 0))
    
    def update(self):
        self.rect.y -= 0.75
        self.opacity -= 2
        self.iteration += 1
        self.image.set_alpha(self.opacity)
        if self.iteration > 120:
            self.kill()
