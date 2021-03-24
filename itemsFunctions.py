from data.gameState import *
from data.player import player
from data.world import roomSize, roomContent,rooms



def nothing():
	print()





def OpenDoor():

    
    from data.items import itemsInfo
    from playerMovement import movePlayer



    playerPosition = player["position"]
    currentRoom = gameState["currentRoom"]

    newPosition = {
        "roomY": currentRoom["Y"],
        "roomX": currentRoom["X"],
        "Y": playerPosition["Y"],
        "X": playerPosition["X"]
    }

    if playerPosition["Y"] == 0:
        
        newPosition["roomY"] -= 1
        newPosition["Y"] = roomSize["Y"] - 2

    elif playerPosition["Y"] == roomSize["Y"] - 1:
        
        newPosition["roomY"] += 1
        newPosition["Y"] = 1

    elif playerPosition["X"] == 0:
        
        newPosition["roomX"] -= 1
        newPosition["X"] = roomSize["X"] - 2

    elif playerPosition["X"] == roomSize["X"] - 1:
        
        newPosition["roomX"] += 1
        newPosition["X"] = 1
    
    movePlayer(newPosition["roomY"], newPosition["roomX"], newPosition["Y"], newPosition["X"])

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