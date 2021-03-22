from data.gameState import *


def nothing():
	print()





def OpenDoor():
    print("Door Opened")

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