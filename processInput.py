

def processInput():

	from render import afterRenderMessage
	from playerMovement import playerWantsToMove
	from data.gameState import gameState
	
	
	Input = input(">>").lower()


	if gameState["gameState"] == 0:

		playerMovement = {"X": 0, "Y": 0}

		if   Input == "d": playerMovement["X"] += 1
		elif Input == "a": playerMovement["X"] -= 1
		elif Input == "w": playerMovement["Y"] -= 1
		elif Input == "s": playerMovement["Y"] += 1
		else:
			afterRenderMessage.append("Command not recognised")

		playerWantsToMove(playerMovement)



	if gameState["gameState"] == 1:

		if len(gameState["pop-upResponses"]) > 0:
			for i in gameState["pop-upResponses"]:

				if Input == i["Code"].lower():
					i["function"]()