import sys

sys.path.insert(0, '/Users/CREEP/Downloads/python/lib')

from background import *
import pygame
import pyautogui

aqua = (25,217,255)
white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)

def shader(surface, mouse, event):
    list = upgradeRect()
    index = 0
    while index <= 2:
        if list[index].collidepoint(mouse):
            shaderSurface = pygame.Surface((400, 70))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                shaderSurface.set_alpha(0)
            else:
                shaderSurface.set_alpha(124)
            shaderSurface.fill(white)
            match index:
                case 0:
                    surface.blit(shaderSurface, (400, 190))
                case 1:
                    surface.blit(shaderSurface, (400, 260))
                case 2:
                    surface.blit(shaderSurface, (400, 330))
            return index
        index += 1
    return 3
            
def buyUpgradeClick(showAlert, event, dog, cost):
    upgradeClick = 1
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if dog >= cost:
            if showAlert:
                pyautogui.alert('dog per click increased by 1')
            return [upgradeClick, 1]
        else:
            pyautogui.alert('not enough dog to purchase. need ' + str(int(cost - dog)) + ' more dog')
    return [0, 0]

def buyUpgradeAuto(showAlert, event, dog, cost):
    upgradeAuto = 10
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if dog >= cost:
            if showAlert:
                pyautogui.alert('dog per second increased by 10')
            return [upgradeAuto, 1]
        else:
            pyautogui.alert('not enough dog to purchase. need ' + str(int(cost - dog)) + ' more dog')
    return [0, 0]

def buyUpgradeMult(showAlert, event, dog, cost):
    upgradeMult = 1.1
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if dog >= cost:
            if showAlert:
                pyautogui.alert('dog profits increased by 1.1')
            return [upgradeMult, 1]
        else:
            pyautogui.alert('not enough dog to purchase. need ' + str(int(cost - dog)) + ' more dog')
    return [1, 0]