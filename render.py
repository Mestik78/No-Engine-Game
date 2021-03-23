import array
import os
import math
import random

from data.items import *
from data.world import roomSize, roomContent, roomRender, renderSizeMultiplier
from data.gameState import gameState
from data.colors import colors



renderStep = 0
afterRenderMessage = []



def getRoomRender():

	for y in range(roomSize["Y"]):

		for x in range(roomSize["X"]):


			for SpriteY in range(renderSizeMultiplier["Y"]):	#por cada sprite

				for SpriteX in range(renderSizeMultiplier["X"]):

					roomRender[y * renderSizeMultiplier["Y"] + SpriteY][x * renderSizeMultiplier["X"] + SpriteX] = colors[itemsInfo[roomContent[y][x]]["color"]] + itemsInfo[roomContent[y][x]]["sprite"][renderStep % len(itemsInfo[roomContent[y][x]]["sprite"])][SpriteY][SpriteX] + colors["end"]	#Añade el subSprite correspondiente



def render():

	clear = lambda: os.system('cls')
	clear()


	getRoomRender()

	#---------renderiza la room
	for y in range(roomSize["Y"] * renderSizeMultiplier["Y"]):
		separator = ''
		print(separator.join(roomRender[y]))



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