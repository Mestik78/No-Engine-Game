import math
import random
import noise

from data.items import *
from data.player import *
from data.world import *

def spawnObject(roomX, roomY, x, y, id):

	roomContent[roomY][roomX][y][x] = id

	roomCollision[roomY][roomX][y][x] = itemsInfo[id]["collision"]



def spawnRandomObject(roomX, roomY, x, y):

	randomObjects = [2,3,5]

	spawnObject(roomX, roomY, x, y, randomObjects[random.randint(0, len(randomObjects) - 1)])



def createRoom(roomY, roomX):

	rooms[roomY][roomX] = True

	for y in range(roomSize["Y"]):

		for x in range(roomSize["X"]):

			spawnObject(roomX, roomY, x,y, 0)	#pone los suelos

			if x == 0 or x == roomSize["X"] - 1 or y == 0 or y == roomSize["Y"] - 1:	#en caso de estar en un borde

				if x == math.floor(roomSize["X"]/2):	#si esta en el medio en X

					spawnObject(roomX, roomY, x, y, 4)	#pone una puerta
					continue

				else:
					spawnObject(roomX, roomY, x, y, 2)	#pone pared
					continue

			
			if x == player["position"]["X"] and y == player["position"]["Y"]:	#coloca al jugador

				spawnObject(roomX, roomY, x, y, 1)

				continue


			if random.random() <= 0.05:	#spawnea un objeto

				spawnRandomObject(roomX, roomY, x, y)




def createPerlinNoise(roomY, roomX):

	rooms[roomY][roomX] = True

	for y in range(roomSize["Y"]):

		for x in range(roomSize["X"]):

			spawnObject(roomX, roomY, x, y, 0)	#pone los suelos


			if (roomY == roomsAmount["Y"] - 1 and y == roomSize["Y"] - 1) or (roomY == 0 and y == 0) or (roomX == roomsAmount["X"] - 1 and x == roomSize["X"] - 1) or (roomX == 0 and x == 0):
				
				spawnObject(roomX, roomY, x, y, 2)	#pone las paredes por el borde de todo el mapa





			noiseValue = (noise.snoise2((roomX * roomSize["X"] + x) / noiseSettings["worldNoise"]["XResolution"] + noiseSettings["worldNoise"]["XOffset"],
								  		(roomY * roomSize["Y"] + y) / noiseSettings["worldNoise"]["YResolution"] + noiseSettings["worldNoise"]["YOffset"]) + 1) / 2

			if noiseValue < 0.2:
				spawnObject(roomX, roomY, x, y, 3) #agua

			elif noiseValue < 0.7:
				spawnObject(roomX, roomY, x, y, 0) #suelo

				grassNoiseValue = (noise.snoise2((roomX * roomSize["X"] + x) / noiseSettings["grassNoise"]["XResolution"] + noiseSettings["grassNoise"]["XOffset"],
									  			 (roomY * roomSize["Y"] + y) / noiseSettings["grassNoise"]["YResolution"] + noiseSettings["grassNoise"]["YOffset"]) + 1) / 2

				if grassNoiseValue < 0.1:
					spawnObject(roomX, roomY, x, y, 5) #grass

			else:
				spawnObject(roomX, roomY, x, y, 2) #montaña



			if y == roomSize["Y"] - 1 or y == 0 or x == roomSize["X"] - 1 or x == 0:
				if itemsInfo[roomContent[roomY][roomX][y][x]]["volatile"]:
					spawnObject(roomX, roomY, x, y, 5) #puertas invisibles


			


def generate(roomY, roomX):
	createPerlinNoise(roomY, roomX)