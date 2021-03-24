import math
from data.world import roomsAmount

gameState = {

    "currentRoom": {
        "X": math.floor(roomsAmount["X"] / 2),
        "Y": math.floor(roomsAmount["Y"] / 2)
    },

    "gameStates": [dict() for x in range(6)],
    "gameState": 0,

    "canMove": True,

    "pop-upText": "If you can see this something went wrong",
    "pop-upResponses": []

}

gameState["gameStates"][0] = {

    "name": "walking",
    "playerCanMove": True

}
gameState["gameStates"][1] = {

    "name": "pop-up",
    "playerCanMove": False

}