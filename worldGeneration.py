import math
import random
#import noise

from data.items import *
from data.player import *
from data.world import roomContent, roomSize, roomRender, roomCollision

def spawnObject(x,y, id):

	roomContent[y][x] = id

	roomCollision[y][x] = itemsInfo[id]["collision"]



def spawnRandomObject(x,y):

	randomObjects = [2,3,5]

	spawnObject(x,y, randomObjects[random.randint(0, len(randomObjects) - 1)])



def createRoom():

	for y in range(roomSize["Y"]):

		for x in range(roomSize["X"]):

			spawnObject(x,y, 0)	#pone los suelos

			if x == 0 or x == roomSize["X"] - 1 or y == 0 or y == roomSize["Y"] - 1:	#en caso de estar en un borde

				if x == math.floor(roomSize["X"]/2):	#si esta en el medio en X

					spawnObject(x,y, 4)	#pone una puerta
					continue

				else:
					spawnObject(x,y, 2)	#pone pared
					continue

			
			if x == player["position"]["X"] and y == player["position"]["Y"]:	#coloca al jugador

				spawnObject(x,y, 1)

				continue


			if random.random() <= 0.05:	#spawnea un objeto

				spawnRandomObject(x,y)




def createPerlinNoise():


	for y in range(roomSize["Y"]):

		for x in range(roomSize["X"]):

			spawnObject(x,y, 0)	#pone los suelos


			if x == player["position"]["X"] and y == player["position"]["Y"]:	#coloca al jugador

				spawnObject(x,y, 1)

				continue


			
			#noise = PerlinNoise()

			
			#if noise([x,y]) > 0.5:

			#	spawnObject(x,y, 2)

			#	continue