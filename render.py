import array
import os
import math
import random

from data.items import *
from data.world import *
from data.gameState import gameState
from data.colors import *
from data.render import Message



renderStep = 0
afterRenderMessage = Message



def getRoomRender():
	
	for y in range(roomSize["Y"]):

		for x in range(roomSize["X"]):

			for SpriteY in range(renderSizeMultiplier["Y"]):	#por cada sprite

				for SpriteX in range(renderSizeMultiplier["X"]):

					roomRenderCellY = y * renderSizeMultiplier["Y"] + SpriteY + 1
					roomRenderCellX = x * renderSizeMultiplier["X"] + SpriteX + 1

					currentRoom =gameState["currentRoom"]
					content = roomContent[currentRoom["Y"]][currentRoom["X"]][y][x]

					roomContentInfo = itemsInfo[content]

					roomContentSprite = roomContentInfo["sprite"]

					color = colors[roomContentInfo["color"]]
					effect = effects[roomContentInfo["effect"]]
					background = backgroundColors[roomContentInfo["backgroundColor"]]

					roomRender[roomRenderCellY][roomRenderCellX] = "\033[" + effect + ";" + color + ";" + background + "m" + roomContentSprite[renderStep % len(roomContentSprite)][SpriteY][SpriteX] + "\u001b[0m"	#Añade el subSprite correspondiente



	for y in range(len(roomRender)):

		for x in range(len(roomRender[y])):

				
			if (x == 0 or x == len(roomRender[y]) - 1) and y != 0 and y != len(roomRender) - 1:
				roomRender[y][x] = "║"
				continue

			if y == 0:
				roomRender[y][x] = "═"

				if x == 0:
					roomRender[y][x] = "╔"
					
				if x == len(roomRender[y]) - 1:
					roomRender[y][x] = "╗"

				continue

			if y == len(roomRender) - 1:
				roomRender[y][x] = "═"

				if x == 0:
					roomRender[y][x] = "╚"
					
				if x == len(roomRender[y]) - 1:
					roomRender[y][x] = "╝"

				continue



def getMinimapRender():
	
	for y in range(len(minimapRender)):

		for x in range(len(minimapRender[y])):

				
			if (x == 0 or x == len(minimapRender[y]) - 1) and y != 0 and y != len(minimapRender) - 1:
				minimapRender[y][x] = "║ "
				continue

			if y == 0:
				minimapRender[y][x] = "══"

				if x == 0:
					minimapRender[y][x] = "╔═"
					
				if x == len(minimapRender[y]) - 1:
					minimapRender[y][x] = "╗"

				continue

			if y == len(minimapRender) - 1:
				minimapRender[y][x] = "══"

				if x == 0:
					minimapRender[y][x] = "╚═"
					
				if x == len(minimapRender[y]) - 1:
					minimapRender[y][x] = "╝"

				continue




			currentRoom = gameState["currentRoom"]

			if x - 1 == currentRoom["X"] and y - 1 == currentRoom["Y"]:
				minimapRender[y][x] = "■"
			else:
				minimapRender[y][x] = "□"



def render():

	clear = lambda: os.system('cls')
	clear()


	getRoomRender()
	getMinimapRender()

	#---------renderiza la room
	for y in range(len(roomRender)):
		separator = ''
		if y < len(minimapRender):
			print(separator.join(roomRender[y]) + "  " + separator.join(minimapRender[y]))
		else:
			print(separator.join(roomRender[y]))



	#---------espaciado
	print()
	print("═" * (roomSize["X"] * renderSizeMultiplier["X"] + 2))



	#---------mensajes
	for i in range(len(afterRenderMessage)):
		print("- " + str(afterRenderMessage[0]))
		del afterRenderMessage[0]

	print()



	#---------dialogo
	if gameState["gameState"] == 1:	#en caso de estar en estado de pop-up
		print("╔" +   "═" * roomSize["X"] * renderSizeMultiplier["X"]   + "╗")

		print(gameState["pop-upText"])


		if len(gameState["pop-upResponses"]) > 0:
			outputString = ""
			for i in gameState["pop-upResponses"]:
				outputString = outputString + i["DisplayName"] + " "
			print(outputString)

		print("╚" +   "═" * roomSize["X"] * renderSizeMultiplier["X"]   + "╝")

		print()



	#---------pregunta
	if gameState["gameState"] == 0:	#en caso de estar en estado de moverse
		print("Where do you want to move next? (W,A,S,D)")

	print()



	global renderStep
	renderStep += 1