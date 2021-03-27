import random


roomSize = {
	"X": 64,
	"Y": 16
}

roomsAmount = {
	"X": 8,
	"Y": 4
}

renderSizeMultiplier = {
	"X": 3,
	"Y": 2
}


noiseSettings = {

	"worldNoise": [
		{
			"strength": 0.75,

			"XOffset": random.randrange(-16384,16384),
			"YOffset": random.randrange(-16384,16384),

			"XResolution": 32,
			"YResolution": 32
		},
		{
			"strength": 0.2,

			"XOffset": random.randrange(-16384,16384),
			"YOffset": random.randrange(-16384,16384),

			"XResolution": 16,
			"YResolution": 16
		},
		{
			"strength": 0.05,

			"XOffset": random.randrange(-16384,16384),
			"YOffset": random.randrange(-16384,16384),

			"XResolution": 8,
			"YResolution": 8
		},
	],
		

	"grassNoise": {
		"XOffset": random.randrange(-16384,16384),
		"YOffset": random.randrange(-16384,16384),

		"XResolution": 16,
		"YResolution": 16
	}

}


rooms = [ [ False for i in range(roomsAmount["X"]) ] for j in range(roomsAmount["Y"]) ]


# X * Y * roomsX * roomsY
roomContent = [ [ [ [ "" for i in range(roomSize["X"]) ] for j in range(roomSize["Y"]) ] for i in range(roomsAmount["X"]) ] for j in range(roomsAmount["Y"]) ]
roomCollision = [ [ [ [ False for i in range(roomSize["X"]) ] for j in range(roomSize["Y"]) ] for i in range(roomsAmount["X"]) ] for j in range(roomsAmount["Y"]) ]

roomRender = [ [ "" for i in range(roomSize["X"] * renderSizeMultiplier["X"] + 2) ] for j in range(roomSize["Y"] * renderSizeMultiplier["Y"] + 2) ]
minimapRender = [ [ "" for i in range(roomsAmount["X"] + 2) ] for j in range(roomsAmount["Y"] + 2) ]