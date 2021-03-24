from itemsFunctions import *

itemsInfo = [dict() for x in range(7)]

itemsInfo[0] = {

	"collision": False,
	"item": "floor",
	"itemName": "a floor",
	"relevant": False,
	"volatile": True,

	"color": "black",
	"backgroundColor": "black",
	"effect": "3",

	"sprite": [[[" ", " ", " "],
			    [" ", " ", " "]]],

	
	"collisionEvent": nothing

}
itemsInfo[1] = {

	"item": "player",
	"collision": False,
	"itemName": "the player",
	"relevant": False,
	"volatile": False,

	"color": "white",
	"backgroundColor": "black",
	"effect": "bold",

	"sprite": [[["ò", " ", "ó"],
			    [" ", "-", " "]]],

	
	"collisionEvent": nothing

}
itemsInfo[2] = {

	"item": "wall",
	"collision": True,
	"itemName": "a wall",
	"relevant": True,
	"volatile": False,

	"color": "white",
	"backgroundColor": "black",
	"effect": "bold",

	"sprite": [[["█", "█", " "],
			    ["█", "█", " "]]],

	
	"collisionEvent": nothing

}
itemsInfo[3] = {

	"item": "water",
	"collision": True,
	"itemName": "water",
	"relevant": True,
	"volatile": False,

	"color": "cyan",
	"backgroundColor": "black",
	"effect": "none",

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
	"volatile": False,

	"color": "red",
	"backgroundColor": "black",
	"effect": "none",

	"sprite": [[["║", "o", "║"],
			    ["║", " ", "║"]]],

	
	"collisionEvent": DoorCollision

}
itemsInfo[5] = {

	"item": "grass",
	"collision": False,
	"itemName": "some grass",
	"relevant": True,
	"volatile": True,

	"color": "green",
	"backgroundColor": "black",
	"effect": "3",

	"sprite": [[[",", ",", ","],
			    [",", ",", ","]]],

	
	"collisionEvent": nothing

}
itemsInfo[6] = {

	"item": "traspasableRoomBorder",
	"collision": False,
	"itemName": "if you are able to see this, somebody didn't do their work right",
	"relevant": False,
	"volatile": False,

	"color": "green",
	"backgroundColor": "black",
	"effect": "none",

	"sprite": [[[" ", " ", " "],
			    [" ", " ", " "]]],

	
	"collisionEvent": OpenDoor

}