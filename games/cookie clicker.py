from functionFile import *
import sys

sys.path.insert(0, '/Users/CREEP/Downloads/python/lib')

from clickText import *
from dogPen import *
from background import *
from text import *
from upgrade import *
from draw import *
from calculations import *
import time
import pygame
import random

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()
pygame.init()
clock = pygame.time.Clock()
dog = 100
dogps = 0

font = pygame.font.SysFont('freesansbold.ttf', 30)
display_width = 800
display_height = 600
displayGame = pygame.display.set_mode((display_width, display_height))
showAlert = True
pygame.display.set_caption("what the dog doin")
vineBoom = pygame.mixer.Sound(r'C:\Users\CREEP\Downloads\python\games\combobreak.wav')

def mainloop():
    global clock
    global dogps
    global dog
    global font
    global showAlert
    dogpc = 1
    costs = [100, 200, 500]
    running = True

    numberGroup = pygame.sprite.Group()
    dogGroup = pygame.sprite.Group()
    allSprites = pygame.sprite.Group()

    dogBg = pygame.image.load(r"C:\Users\CREEP\Downloads\python\games\assets\bgBlue.jpg")
    dogBg = pygame.transform.scale(dogBg, (400, 600))
    dogPic = pygame.image.load(r"C:\Users\CREEP\Downloads\python\games\dog images\dog.jpg")
    dogPic = pygame.transform.scale(dogPic, (150, 200))
    dogPic = pygame.transform.rotate(dogPic, 270)
    dogPenBg = pygame.image.load(r"C:\Users\CREEP\Downloads\python\games\assets\bgRed.jpg")
    dogPenBg = pygame.transform.scale(dogPenBg, (400, 200))
    upgradeBg = pygame.image.load(r"C:\Users\CREEP\Downloads\python\games\assets\StoreButton.jpg")
    upgradeBg = pygame.transform.scale(upgradeBg, (400, 70))
    dogArea = pygame.rect.Rect(100, 250, 200, 150)

    moment = time.time()
    loaded = False

    while running:
        if running:
            random.seed()
            displayGame.fill((255, 255, 255))
            drawBackground(displayGame, costs)
            if time.time() > moment + 0.1:
                dog += dogps/10
                moment = time.time()
            mouse = pygame.mouse.get_pos()
            if loaded:
                toUpgrade = shader(displayGame, mouse, event)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if loaded and toUpgrade >= 0 and toUpgrade <= 2 and event.type == pygame.MOUSEBUTTONDOWN:
                    match toUpgrade:
                        case 0:
                            purchaseState = buyUpgradeAuto(showAlert, event, dog, costs[0])
                            dogps += purchaseState[0]
                            if purchaseState[1]:
                                dog -= costs[0]
                                costs[0] *= 1.15
                        case 1:
                            purchaseState = buyUpgradeClick(showAlert, event, dog, costs[1])
                            dogpc += purchaseState[0]
                            if purchaseState[1]:
                                dog -= costs[1]
                                costs[1] *= 1.15
                        case 2:
                            purchaseState = buyUpgradeMult(showAlert, event, dog, costs[2])
                            dogps *= purchaseState[0]
                            dogpc *= purchaseState[0]
                            if purchaseState[1]:
                                dog -= costs[2]
                                costs[2] *= 1.15
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if dogArea.collidepoint(mouse) and event.button == 1:
                        dog += dogpc
                        randX = random.randint(-10, 10)
                        randY = random.randint(-10, 10)
                        randCoord = addCoord(mouse, (randX, randY))
                        onClick = clickText(round(dogpc, 2), 20, white, randCoord[0], randCoord[1])
                        randX = random.randint(450, 750)
                        randY = random.randint(450, 550)
                        dogPop = dogPen(randX, randY)
                        numberGroup.add(onClick)
                        allSprites.add((onClick, dogPop))
                        dogGroup.add(dogPop)
                        #pygame.mixer.Sound.play(pygame.mixer.Sound("C:\\Users\\CREEP\\Downloads\\python\\games\\boom.mp3"))
                        # #pygame.mixer.music.stop()
                        #vineBoom.play()
                        #time.sleep(1)
                        #vineBoom.stop()
                    if alertSwitch.collidepoint(mouse) and event.button == 1:
                        showAlert = not showAlert
                        print(showAlert)
            dogAmt = Text(str(convertDecimal(dog)), 200, 170, 40)
            dogAmt.Draw(displayGame)
            DrawText(displayGame, "Dog per second: " + convertDecimal(dogps), black, light_grey, 200, 215, 20)
            alertSwitch = DrawTextLeftCorner(displayGame, "Show Alerts: " + str(showAlert), white, aqua, 0, 600, 20)
            allSprites.update()
            allSprites.draw(displayGame)
            loaded = True
            pygame.display.flip()
            clock.tick(60)

    
mainloop()
