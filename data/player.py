import math
from data.world import roomSize


player = {
	
	"position": {
		"roomX": 0,
		"roomY": 0,
		"X": 1,
		"Y": 1
	},
	"itemBelow": 0

}




player["position"]["X"] = math.floor(roomSize["X"] / 2)
player["position"]["Y"] = math.floor(roomSize["Y"] / 2)