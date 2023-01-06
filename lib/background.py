import pygame
import sys

sys.path.insert(0, '/Users/CREEP/Downloads/python/lib')
from dogPen import dogPen
from draw import *

aqua = (25,217,255)
white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)
light_grey = (224, 224, 224)
light_blue = (173, 216, 230)
light_pink = (211, 107, 129)
light_brown = (175, 152, 97)
blue = (0, 100, 250)

dogBg = pygame.image.load(r"C:\Users\CREEP\Downloads\python\games\assets\bgBlue.jpg")
dogBg = pygame.transform.scale(dogBg, (400, 600))
dogPic = pygame.image.load(r"C:\Users\CREEP\Downloads\python\games\dog images\dog.jpg")
dogPic = pygame.transform.scale(dogPic, (150, 200))
dogPic = pygame.transform.rotate(dogPic, 270)
dogPenBg = pygame.image.load(r"C:\Users\CREEP\Downloads\python\games\assets\bgBlue.jpg")
dogPenBg = pygame.transform.scale(dogPenBg, (400, 200))
upgradeBg = pygame.image.load(r"C:\Users\CREEP\Downloads\python\games\assets\StoreButton.jpg")
upgradeBg = pygame.transform.scale(upgradeBg, (400, 70))
labelBg = pygame.image.load(r"C:\Users\CREEP\Downloads\python\games\assets\bgBlue.jpg")
labelBg = pygame.transform.scale(labelBg, (400, 200))

def drawBackground(display, costs):
    display.blit(dogBg, (0, 0))
    display.blit(dogPic, (100, 250))
    display.blit(dogPenBg, (400, 400))
    display.blit(labelBg, (400, 0))
    dogPenRect = pygame.Surface((400, 200))
    dogPenRect.set_alpha(130)
    dogPenRect.fill(light_pink)
    upgradeRect = pygame.Surface((400, 190))
    upgradeRect.set_alpha(130)
    upgradeRect.fill(light_brown)
    display.blit(upgradeRect, (400, 0))
    DrawText(display, "Dog: ", black, light_grey, 200, 100, 80)
    drawBorder(100, 400, 200, 150, black, display)
    pygame.draw.line(display, black, (400, 0), (400, 600))
    pygame.draw.line(display, black, (400, 400), (800, 400))
    DrawText(display, "Upgrades", black, light_grey, 600, 100, 80)
    dogRect = pygame.Surface((400, 40))
    dogRect.set_alpha(124)
    dogRect.fill(light_grey)
    display.blit(dogRect, (0, 150))
    display.blit(dogPenRect, (400, 400))
    display.blit(upgradeBg, (400, 190))
    display.blit(upgradeBg, (400, 260))
    display.blit(upgradeBg, (400, 330))
    upgradeText(display, costs)

def upgradeRect():
    upgradeAuto = upgradeBg.get_rect(center=(600, 225))
    upgradeClick = upgradeBg.get_rect(center=(600, 295))
    upgradeMult = upgradeBg.get_rect(center=(600, 365))
    list = [upgradeAuto, upgradeClick, upgradeMult]
    return list