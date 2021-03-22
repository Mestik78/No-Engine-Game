import math
from data.world import roomSize


player = {
	
	"position": {
		"X": 0,
		"Y": 0
	},
	"itemBelow": 0

}




player["position"]["X"] = math.floor(roomSize["X"] / 2)
player["position"]["Y"] = math.floor(roomSize["Y"] / 2)