from data.gameState import *
from data.player import player
from data.world import roomSize



def nothing():
	print()





def OpenDoor():

    
    from playerMovement import movePlayer



    playerPosition = player["position"]
    currentRoom = gameState["currentRoom"]

    if playerPosition["Y"] == 0:
        movePlayer(currentRoom["Y"] - 1, currentRoom["X"], roomSize["Y"] - 2, playerPosition["X"])
        currentRoom["Y"] -= 1

    elif playerPosition["Y"] == roomSize["Y"] - 1:
        movePlayer(currentRoom["Y"] + 1, currentRoom["X"], 1, playerPosition["X"])
        currentRoom["Y"] += 1

    elif playerPosition["X"] == 0:
        movePlayer(currentRoom["Y"], currentRoom["X"] - 1, playerPosition["Y"], roomSize["X"] - 2)
        currentRoom["X"] -= 1

    elif playerPosition["X"] == roomSize["X"] - 1:
        movePlayer(currentRoom["Y"], currentRoom["X"] + 1, playerPosition["Y"], 1)
        currentRoom["X"] += 1
    
    gameState["gameState"] = 0
    

def DontOpenDoor():
	gameState["gameState"] = 0


def DoorCollision():
    gameState["gameState"] = 1
    gameState["pop-upText"] = "Do you want to open the door?"

    gameState["pop-upResponses"] = [dict() for x in range(2)]


    gameState["pop-upResponses"][0] = {
        "Code": "Y",
        "DisplayName": "Yes (Y)",
        "function": OpenDoor
    }
        
    gameState["pop-upResponses"][1] = {
        "Code": "N",
        "DisplayName": "No (N)",
        "function": DontOpenDoor
        }