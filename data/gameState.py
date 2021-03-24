gameState = {

    "currentRoom": {
        "X": 0,
        "Y": 0
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