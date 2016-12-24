import pygame, sys, random
from pygame.locals import *


fpsClock=pygame.time.Clock()

pygame.display.set_caption('MichaelCraft')
pygame.display.set_icon(pygame.image.load('player.png'))

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
                DIRT   : pygame.image.load('dirt.png'),
                GRASS  : pygame.image.load('grass.png'),
                WATER  : pygame.image.load('water.png'),
                COAL   : pygame.image.load('coal.png'),
                CLOUD  : pygame.image.load('cloud.png')
            }

inventory =   {
                DIRT   : 0,
                GRASS  : 0,
                WATER  : 0,
                COAL   : 0
            }

#useful game dimensions
TILESIZE  = 40
MAPWIDTH  = 30
MAPHEIGHT = 15

#the player image
PLAYER = pygame.image.load('player.png')
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

while True:
    DISPLAYSURF.fill(BLACK)

    #get all the user events
    for event in pygame.event.get():
        #if the user wants to quit
        if event.type == QUIT:
            #and the game and close the window
            pygame.quit()
            sys.exit()
        #if a key is pressed
        elif event.type == KEYDOWN:
            #if the right arrow is pressed
            if event.key == K_RIGHT and playerPos[0] <  MAPWIDTH - 1:
                #change the player's x position
                playerPos[0] += 1
            if event.key == K_LEFT and playerPos[0] >  0:
                #change the player's x position
                playerPos[0] -= 1
            if event.key == K_UP and playerPos[1] >  0:
                #change the player's x position
                playerPos[1] -= 1
            if event.key == K_DOWN and playerPos[1] <  MAPHEIGHT -1:
                #change the player's x position
                playerPos[1] += 1
            if event.key == K_SPACE:
                #what resource is the player standing on?
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                #player now has 1 more of this resource
                inventory[currentTile] += 1
                #the player is now standing on dirt
                tilemap[playerPos[1]][playerPos[0]] = DIRT

            #placing dirt
            if (event.key == K_1):
                #get the tile to swap with the dirt
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                #if we have dirt in our inventory
                if inventory[DIRT] >  0:
                    #remove one dirt and place it
                    inventory[DIRT] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = DIRT
                    #swap the item that was there before
                    inventory[currentTile] += 1
            #placing grass
            if (event.key == K_2):
                #get the tile to swap with the grass
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                #if we have dirt in our inventory
                if inventory[GRASS] >  0:
                    #remove one grass and place it
                    inventory[GRASS] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = GRASS
                    #swap the item that was there before
                    inventory[currentTile] += 1
            #placing water
            if (event.key == K_3):
                #get the tile to swap with the water
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                #if we have dirt in our inventory
                if inventory[WATER] >  0:
                    #remove one dirt and place it
                    inventory[WATER] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = WATER
                    #swap the item that was there before
                    inventory[currentTile] += 1
            #placing coal
            if (event.key == K_4):
                #get the tile to swap with the dirt
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                #if we have coal in our inventory
                if inventory[COAL] >  0:
                    #remove one coal and place it
                    inventory[COAL] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = COAL
                    #swap the item that was there before
                    inventory[currentTile] += 1

    #loop through each row
    for row in range(MAPHEIGHT):
        #loop through each column in the row
        for column in range(MAPWIDTH):
            #draw the resource at that position in the tilemap, using the correct image
            DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))

    #display the player at the correct position
    DISPLAYSURF.blit(PLAYER,(playerPos[0]*TILESIZE,playerPos[1]*TILESIZE))

    #display the inventory, starting 10 pixels in
    placePosition = 10
    for item in resources:
        #add the image
        DISPLAYSURF.blit(textures[item],(placePosition,MAPHEIGHT*TILESIZE+20))
        placePosition += 30
        #add the text showing the amount in the inventory
        textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj,(placePosition,MAPHEIGHT*TILESIZE+20))
        placePosition += 50
    #display cloud1
    DISPLAYSURF.blit(textures[CLOUD].convert_alpha(), (cloudx1, cloudy1))
    cloudx1+=3
    if cloudx1 > MAPWIDTH*TILESIZE:
        cloudy1= random.randint(0, MAPHEIGHT*TILESIZE-200)
        cloudx1= -200

    DISPLAYSURF.blit(textures[CLOUD].convert_alpha(), (cloudx2, cloudy2))
    cloudx2+=2
    if cloudx2 > MAPWIDTH*TILESIZE:
        cloudy2= random.randint(0, MAPHEIGHT*TILESIZE-200)
        cloudx2= -200


    #update the display
    pygame.display.update()
    fpsClock.tick(24)
