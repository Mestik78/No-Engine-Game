
roomSize = {
	"X": 30,
	"Y": 10
}

renderSizeMultiplier = {
	"X": 3,
	"Y": 2
}




roomContent = [ [ "" for i in range(roomSize["X"]) ] for j in range(roomSize["Y"]) ]
roomRender = [ [ "" for i in range(roomSize["X"] * renderSizeMultiplier["X"]) ] for j in range(roomSize["Y"] * renderSizeMultiplier["Y"]) ]
roomCollision = [ [ False for i in range(roomSize["X"]) ] for j in range(roomSize["Y"]) ]