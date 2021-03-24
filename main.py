import array
import os
import math
import random
import time



from render import render
from worldGeneration import generate
from processInput import processInput



generate(0,0)



while True:	#game loop

	render()
	processInput()

