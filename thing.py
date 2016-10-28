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
			#Moving
			if (event.key==K_RIGHT) and playerPos[0]<mapwidth-1:
				playerPos[0]+=1
			if (event.key==K_LEFT) and playerPos[0]>0:
				playerPos[0]-=1
			if (event.key==K_DOWN) and playerPos[1]<mapheight-1:
				playerPos[1]+=1
			if (event.key==K_UP) and playerPos[1]>0:
				playerPos[1]-=1
			#Pick up dem hot tiles
			if event.key==K_SPACE:
				currentTile=tilemap[playerPos[1]][playerPos[0]]
				inventory[currentTile]+=1
				tilemap[playerPos[1]][playerPos[0]]=dirt


	#Display
	for row in range(mapheight):
		for column in range(mapwidth):
			display.blit(textures[tilemap[row][column]],(column*tilesize,row*tilesize))
	#Display player
	display.blit(player,(playerPos[0]*tilesize,playerPos[1]*tilesize))

	#Display the inventory, starting 10 pixels in
	placePosition = 10
	for item in resources:
		#add the image
		display.blit(textures[item],(placePosition,MAPHEIGHT*TILESIZE+20))
		placePosition += 30
		#add the text showing the amount in the inventory
		textObj = invfont.render(str(inventory[item]), True, white, black)
		display.blit(textObj,(placePosition,mapheight*tilesize+20))
		placePosition += 50
	#Updates Display
	pygame.display.update()
