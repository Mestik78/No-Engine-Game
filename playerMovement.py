from render import afterRenderMessage
from data.world import *
from data.player import *
from data.items import *
from data.gameState import gameState


def afterMovement():
	itemsInfo[player["itemBelow"]]["collisionEvent"]()


def movePlayer(direction):

	if player["position"]["Y"] + direction["Y"] < roomSize["Y"] and player["position"]["X"] + direction["X"] < roomSize["X"]:	#en caso de que no se salga del mapa

		if roomCollision[player["position"]["Y"] + direction["Y"]][player["position"]["X"] + direction["X"]] == False:

			roomContent[player["position"]["Y"]][player["position"]["X"]] = player["itemBelow"]	#quita al jugador y pone el item que tenga debajo

			player["position"]["X"] += direction["X"]
			player["position"]["Y"] += direction["Y"]

			player["itemBelow"] = roomContent[player["position"]["Y"]][player["position"]["X"]] #guarda el item debajo del jugador
			roomContent[player["position"]["Y"]][player["position"]["X"]] = 1	#pone al jugador en la nueva posición


			if direction["X"] == 1:  afterRenderMessage.append("You moved east")
			if direction["X"] == -1: afterRenderMessage.append("You moved west")
			if direction["Y"] == 1:  afterRenderMessage.append("You moved south")
			if direction["Y"] == -1: afterRenderMessage.append("You moved north")


			if itemsInfo[player["itemBelow"]]["relevant"]:
				afterRenderMessage.append("You found " + itemsInfo[player["itemBelow"]]["itemName"])

			afterMovement()

		else:

			if direction["X"] == 1:  afterRenderMessage.append("You tried to move east")
			if direction["X"] == -1: afterRenderMessage.append("You tried to move west")
			if direction["Y"] == 1:  afterRenderMessage.append("You tried to move south")
			if direction["Y"] == -1: afterRenderMessage.append("You tried to move north")

			afterRenderMessage.append("You can't pass, there's " + itemsInfo[roomContent[player["position"]["Y"] + direction["Y"]][player["position"]["X"] + direction["X"]]]["itemName"])
