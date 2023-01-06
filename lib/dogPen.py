import pygame
import random

pic1 = pygame.image.load(r"C:\Users\CREEP\Downloads\python\games\dog images\dog1.jpg")
pic2 = pygame.image.load(r"C:\Users\CREEP\Downloads\python\games\dog images\dog2.jpg")
pic3 = pygame.image.load(r"C:\Users\CREEP\Downloads\python\games\dog images\dog3.jpg")
pic4 = pygame.image.load(r"C:\Users\CREEP\Downloads\python\games\dog images\dog4.jpg")
pic5 = pygame.image.load(r"C:\Users\CREEP\Downloads\python\games\dog images\dog5.jpg")

class dogPen(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.iteration = 0        
        self.opacity = 255
        index = random.randint(0, 4)
        picture1 = pygame.transform.scale(pic1, (100, 100))
        picture2 = pygame.transform.scale(pic2, (100, 100))
        picture3 = pygame.transform.scale(pic3, (100, 100))
        picture4 = pygame.transform.scale(pic4, (100, 100))
        picture5 = pygame.transform.scale(pic5, (100, 100))
        pics = [picture1, picture2, picture3, picture4, picture5]
        self.image = pics[index]
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.iteration += 1
        self.opacity -= 2
        self.image.set_alpha(self.opacity)
        if self.opacity <= 0:
            self.kill()