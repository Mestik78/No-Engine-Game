import array
import os
import math
import random
import time



from render import render
from worldGeneration import generate
from processInput import processInput
from data.gameState import gameState

currentRoom = gameState["currentRoom"]

generate(currentRoom["Y"], currentRoom["X"])



while True:	#game loop

	render()
	processInput()

