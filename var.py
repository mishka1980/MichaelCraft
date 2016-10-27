import pygame,sys
#resources
dirt=0
grass=1
water=2
coal=3

#a dictionary resources to textures
textures = {
		grass: pygame.image.load('grass.png'),
		dirt: pygame.image.load('dirt.png'),
		water: pygame.image.load('water.png'),
		coal: pygame.image.load('coal.png')
	}
#tile size
tilesize=40
#map width and height
mapwidth=10
mapheight=10
#Random tilemap generation, Set to all dirt
tilemap=[ [dirt for w in range(mapwidth)] for h in range(mapheight)]
#Weghted tilemap generation
import random
for rw in range(mapheight):
	for cl in range(mapwidth):
		randomNumber=random.randint(0,15)
		if randomNumber==0:
			tile=coal
		elif randomNumber==1 or randomNumber==2:
			tile=water
		elif randomNumber>=3 and randomNumber<=7:
			tile=grass
		else:
			tile=dirt

		tilemap[rw][cl]=tile


from pygame.locals import *
#Initialize Pygame
pygame.init()
#Init Display
display=pygame.display.set_mode((mapwidth*tilesize,mapheight*tilesize))
#Display Name
pygame.display.set_caption("Game")


#player image
player=pygame.image.load("player.png").convert_alpha()
#player pos
playerPos=[0,0]
