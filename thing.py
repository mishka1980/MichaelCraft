import pygame,sys
from var import *

#Event loop (runs until quit)
while True:
	for event in pygame.event.get():

		#Checks if you want to quit
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
		elif event.type==KEYDOWN:
			if (event.key==K_RIGHT) and playerPos[0]<mapwidth-1:
				playerPos[0]+=1
			if (event.key==K_LEFT) and playerPos[0]>0:
				playerPos[0]-=1
			if (event.key==K_DOWN):
				playerPos[1]+=1
			if (event.key==K_UP) and playerPos[1]<mapheight-1:
				playerPos[1]-=1

	#Display
	for row in range(mapheight):
		for column in range(mapwidth):
			display.blit(textures[tilemap[row][column]],(column*tilesize,row*tilesize))
	display.blit(player,(playerPos[0]*tilesize,playerPos[1]*tilesize))
	#Updates Display
	pygame.display.update()
