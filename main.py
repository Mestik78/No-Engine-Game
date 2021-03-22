import array
import os
import math
import random
import time



from render import render, afterRenderMessage
from worldGeneration import createRoom, createPerlinNoise
from processInput import processInput



createRoom()



def GameLoop():

	render()
	processInput()


	GameLoop()


GameLoop()