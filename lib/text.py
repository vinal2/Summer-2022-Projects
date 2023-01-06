import pygame
class Text:
    """Centered Text Class"""
    # Constructror
    def __init__(self, text, x, y, size, color = (0,0,0),):
        super().__init__()
        self.x = x #Horizontal center of box
        self.y = y #Vertical center of box
        # Start PyGame Font
        pygame.font.init()
        font = pygame.font.Font('freesansbold.ttf', size)
        self.txt = font.render(text, True, color)
        self.size = font.size(text) #(width, height)
    # Draw Method
    def Draw(self, screen):
        drawX = self.x - (self.size[0] / 2.)
        drawY = self.y - (self.size[1] / 2.)
        coords = (drawX, drawY)
        screen.blit(self.txt, coords)