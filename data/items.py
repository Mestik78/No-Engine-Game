from itemsFunctions import *

itemsInfo = [dict() for x in range(6)]

itemsInfo[0] = {

	"collision": False,
	"item": "floor",
	"itemName": "a floor",
	"relevant": False,

	"color": "black",
	"sprite": [[[" ", " ", " "],
			    [" ", " ", " "]]],

	
	"collisionEvent": nothing

}
itemsInfo[1] = {

	"item": "player",
	"collision": False,
	"itemName": "the player",
	"relevant": False,

	"color": "white",
	"sprite": [[["ò", " ", "ó"],
			    [" ", "-", " "]]],

	
	"collisionEvent": nothing

}
itemsInfo[2] = {

	"item": "wall",
	"collision": True,
	"itemName": "a wall",
	"relevant": True,

	"color": "white",
	"sprite": [[["█", "█", " "],
			    ["█", "█", " "]]],

	
	"collisionEvent": nothing

}
itemsInfo[3] = {

	"item": "water",
	"collision": True,
	"itemName": "water",
	"relevant": True,

	"color": "cyan",
	"sprite": [[["/", "/", "/"],
			    ["/", "/", "/"]],

			   [["\\", "\\", "\\"],
			    ["\\", "\\", "\\"]]],

	
	"collisionEvent": nothing

}
itemsInfo[4] = {

	"item": "door",
	"collision": False,
	"itemName": "a door",
	"relevant": True,

	"color": "red",
	"sprite": [[["║", "o", "║"],
			    ["║", " ", "║"]]],

	
	"collisionEvent": DoorCollision

}
itemsInfo[5] = {

	"item": "grass",
	"collision": False,
	"itemName": "some grass",
	"relevant": True,

	"color": "green",
	"sprite": [[[",", ",", ","],
			    [",", ",", ","]]],

	
	"collisionEvent": nothing

}