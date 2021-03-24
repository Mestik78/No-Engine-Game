import math
from data.world import roomSize, roomsAmount


player = {
	
	"position": {
		"roomX": 0,
		"roomY": 0,
		"X": 1,
		"Y": 1
	},
	"itemBelow": 0

}



player["position"]["roomX"] = math.floor(roomsAmount["X"] / 2)
player["position"]["roomY"] = math.floor(roomsAmount["Y"] / 2)

player["position"]["X"] = math.floor(roomSize["X"] / 2)
player["position"]["Y"] = math.floor(roomSize["Y"] / 2)