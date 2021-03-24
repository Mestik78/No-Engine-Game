import array
import os
import math
import random

from data.items import *
from data.world import *
from data.gameState import gameState
from data.colors import colors
from data.render import Message



renderStep = 0
afterRenderMessage = Message



def getRoomRender():
	
	for y in range(roomSize["Y"]):

		for x in range(roomSize["X"]):


			for SpriteY in range(renderSizeMultiplier["Y"]):	#por cada sprite

				for SpriteX in range(renderSizeMultiplier["X"]):

					roomRenderCellY = y * renderSizeMultiplier["Y"] + SpriteY
					roomRenderCellX = x * renderSizeMultiplier["X"] + SpriteX

					currentRoom =gameState["currentRoom"]
					content = roomContent[currentRoom["Y"]][currentRoom["X"]][y][x]

					roomContentInfo = itemsInfo[content]

					roomContentSprite = roomContentInfo["sprite"]

					color = colors[roomContentInfo["color"]]

					roomRender[roomRenderCellY][roomRenderCellX] = color + roomContentSprite[renderStep % len(roomContentSprite)][SpriteY][SpriteX] + colors["end"]	#Añade el subSprite correspondiente


def getMinimapRender():
	
	for y in range(roomsAmount["Y"]):

		for x in range(roomsAmount["X"]):

			currentRoom = gameState["currentRoom"]

			if x == currentRoom["X"] and y == currentRoom["Y"]:
				minimapRender[y][x] = "■"
			else:
				minimapRender[y][x] = "□"



def render():

	clear = lambda: os.system('cls')
	clear()


	getRoomRender()
	getMinimapRender()

	#---------renderiza la room
	for y in roomRender:
		separator = ''
		print(separator.join(y))

	print()

	for y in minimapRender:
		separator = ''
		print(separator.join(y))



	#---------espaciado
	print()
	print("═" * roomSize["X"] * renderSizeMultiplier["X"])



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