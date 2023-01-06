import sys
import text

sys.path.insert(0, '/Users/CREEP/Downloads/python/lib')
import pygame
from calculations import *

def DrawTextLeftCorner(surface, text, Textcolor, Rectcolor, x, y, fsize):
    font = pygame.font.Font('freesansbold.ttf', fsize)
    text = font.render(text, True, Textcolor, Rectcolor)
    textRect = text.get_rect()
    textRect.bottomleft = (x, y)
    surface.blit(text, textRect)
    return textRect

def rectangle(display, color, x, y, w, h):
    pygame.draw.rect(display, color, (x, y, w, h))

def DrawText(surface, text, Textcolor, Rectcolor, x, y, fsize):
    font = pygame.font.Font('freesansbold.ttf', fsize)
    text = font.render(text, True, Textcolor, Rectcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    surface.blit(text, textRect)
    return textRect

def drawBorder(cornerX, cornerY, width, height, color, displayGame):
    pygame.draw.line(displayGame, color, (cornerX, cornerY), (cornerX + width, cornerY))
    pygame.draw.line(displayGame, color, (cornerX, cornerY), (cornerX, cornerY - height))
    pygame.draw.line(displayGame, color, (cornerX, cornerY - height), (cornerX + width, cornerY - height))
    pygame.draw.line(displayGame, color, (cornerX + width, cornerY), (cornerX + width, cornerY - height))

def upgradeText(surface, costs):
    upgrade1name = text.Text("Auto Clicker", 480, 225, 20)
    upgrade2name = text.Text("Click Upgrade", 490, 295, 20)
    upgrade3name = text.Text("Dog Multiplier", 490, 365, 20)
    upgrade1cost = text.Text(str(convertDecimal(costs[0])) + " dog", 727, 225, 20)
    upgrade2cost = text.Text(str(convertDecimal(costs[1])) + " dog", 727, 295, 20)
    upgrade3cost = text.Text(str(convertDecimal(costs[2])) + " dog", 727, 365, 20)
    upgrade1name.Draw(surface)
    upgrade2name.Draw(surface)
    upgrade3name.Draw(surface)
    upgrade1cost.Draw(surface)
    upgrade2cost.Draw(surface)
    upgrade3cost.Draw(surface)