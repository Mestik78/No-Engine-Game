from render import afterRenderMessage
from data.world import *
from data.player import *
from data.gameState import gameState
from worldGeneration import generate


from data.items import *
def afterMovement():

	itemsInfo[player["itemBelow"]]["collisionEvent"]()

	
	if itemsInfo[player["itemBelow"]]["relevant"]:
		afterRenderMessage.append("You found " + itemsInfo[player["itemBelow"]]["itemName"])


def movePlayer(roomY, roomX, y, x):

	if rooms[roomY][roomX] == False:
		generate(roomY, roomX)


		
	content = roomContent[roomY][roomX]
	playerPosition = player["position"]

	currentRoom = gameState["currentRoom"]



	if itemsInfo[content[y][x]]["collision"] == False:

		roomContent[currentRoom["Y"]][currentRoom["X"]][playerPosition["Y"]][playerPosition["X"]] = player["itemBelow"]	#quita al jugador y pone el item que tenga debajo

		playerPosition["roomX"] = roomX
		playerPosition["roomY"] = roomY

		playerPosition["X"] = x
		playerPosition["Y"] = y

		player["itemBelow"] = content[playerPosition["Y"]][playerPosition["X"]] #guarda el item debajo del jugador
		content[playerPosition["Y"]][playerPosition["X"]] = 1	#pone al jugador en la nueva posición


		gameState["currentRoom"]["X"] = roomX
		gameState["currentRoom"]["Y"] = roomY

	

		afterMovement()


def playerWantsToMove(direction):


	currentRoom = gameState["currentRoom"]
	playerPosition = player["position"]

	if playerPosition["Y"] + direction["Y"] < roomSize["Y"] and playerPosition["Y"] + direction["Y"] >= 0 and playerPosition["X"] + direction["X"] < roomSize["X"] and playerPosition["X"] + direction["X"] >= 0:	#en caso de que no se salga del mapa

		collision = roomCollision[currentRoom["Y"]][currentRoom["X"]]
		content = roomContent[currentRoom["Y"]][currentRoom["X"]]

		if collision[playerPosition["Y"] + direction["Y"]][playerPosition["X"] + direction["X"]] == False:

			movePlayer(currentRoom["Y"], currentRoom["X"], playerPosition["Y"] + direction["Y"], playerPosition["X"] + direction["X"])

			if direction["X"] == 1:  afterRenderMessage.append("You moved east")
			if direction["X"] == -1: afterRenderMessage.append("You moved west")
			if direction["Y"] == 1:  afterRenderMessage.append("You moved south")
			if direction["Y"] == -1: afterRenderMessage.append("You moved north")


		else:

			if direction["X"] == 1:  afterRenderMessage.append("You tried to move east")
			if direction["X"] == -1: afterRenderMessage.append("You tried to move west")
			if direction["Y"] == 1:  afterRenderMessage.append("You tried to move south")
			if direction["Y"] == -1: afterRenderMessage.append("You tried to move north")

			afterRenderMessage.append("You can't pass, there's " + itemsInfo[content[playerPosition["Y"] + direction["Y"]][playerPosition["X"] + direction["X"]]]["itemName"])
