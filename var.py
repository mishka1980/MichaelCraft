import pygame, sys, random
from pygame.locals import *


fpsClock=pygame.time.Clock()

pygame.display.set_caption('MichaelCraft')
pygame.display.set_icon(pygame.image.load('images/player.png'))

#constants representing colours
BLACK = (0, 0,  0  )
BROWN = (153, 76,  0  )
GREEN = (0,   255, 0  )
BLUE  = (0,   0,   255)
WHITE = (255,   255,   255)

#cloud position
cloudx1= -200
cloudy1= 0

cloudx2= -200
cloudy2= 300

#constants representing the different resources
DIRT  = 0
GRASS = 1
WATER = 2
COAL  = 3
CLOUD = 4

#a dictionary linking resources to textures
textures =   {
                DIRT   : pygame.image.load('images/dirt.png'),
                GRASS  : pygame.image.load('images/grass.png'),
                WATER  : pygame.image.load('images/water.png'),
                COAL   : pygame.image.load('images/coal.png'),
                CLOUD  : pygame.image.load('images/cloud.png')
            }

inventory =   {
                DIRT   : 0,
                GRASS  : 0,
                WATER  : 0,
                COAL   : 0
            }

#useful game dimensions


TILESIZE  = 40
MAPWIDTH=20
MAPHEIGHT=15

import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *


#the player image
PLAYER = pygame.image.load('images/player.png')
#the position of the player [x,y]
playerPos = [0,0]

#a list of resources
resources = [DIRT,GRASS,WATER,COAL]
#use list comprehension to create our tilemap
tilemap = [ [DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT) ]

#set up the display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE + 80))

#add a font for our inventory
INVFONT = pygame.font.SysFont("comicsansms", 72)

#loop through each row
for rw in range(MAPHEIGHT):
    #loop through each column in that row
    for cl in range(MAPWIDTH):
        #pick a random number between 0 and 15
        randomNumber = random.randint(0,15)
        #if a zero, then the tile is coal
        if randomNumber == 0:
            tile = COAL
        #water if the random number is a 1 or a 2
        elif randomNumber == 1 or randomNumber == 2:
            tile = WATER
        elif randomNumber >= 3 and randomNumber <= 7:
            tile = GRASS
        else:
            tile = DIRT
        #set the position in the tilemap to the randomly chosen tile
        tilemap[rw][cl] = tile
