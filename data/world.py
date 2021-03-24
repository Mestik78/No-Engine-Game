import random


roomSize = {
	"X": 50,
	"Y": 20
}

roomsAmount = {
	"X": 5,
	"Y": 5
}

renderSizeMultiplier = {
	"X": 3,
	"Y": 2
}


noiseSettings = {

	"worldNoise": {
		"XOffset": random.randrange(-16384,16384),
		"YOffset": random.randrange(-16384,16384),

		"XResolution": 16,
		"YResolution": 16
	},

	"grassNoise": {
		"XOffset": random.randrange(-16384,16384),
		"YOffset": random.randrange(-16384,16384),

		"XResolution": 8,
		"YResolution": 8
	}

}


rooms = [ [ False for i in range(roomsAmount["X"]) ] for j in range(roomsAmount["Y"]) ]


# X * Y * roomsX * roomsY
roomContent = [ [ [ [ "" for i in range(roomSize["X"]) ] for j in range(roomSize["Y"]) ] for i in range(roomsAmount["X"]) ] for j in range(roomsAmount["Y"]) ]
roomCollision = [ [ [ [ False for i in range(roomSize["X"]) ] for j in range(roomSize["Y"]) ] for i in range(roomsAmount["X"]) ] for j in range(roomsAmount["Y"]) ]

roomRender = [ [ "" for i in range(roomSize["X"] * renderSizeMultiplier["X"]) ] for j in range(roomSize["Y"] * renderSizeMultiplier["Y"]) ]
minimapRender = [ [ "" for i in range(roomsAmount["X"]) ] for j in range(roomsAmount["Y"]) ]