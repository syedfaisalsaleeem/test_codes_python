def modify_players(Selector1,Selector2):

	count = 0
	Selector1[0] = "faisal saleem"
	Selector1[1] = "asad babar"
	Selector1[2] = "ali shafique"
	for i in range(len(Selector1)):
		Selector1[i] = Selector1[i].capitalize()

	Selector2[0] = "ali raza"
	Selector2[1] = "Virat Kohli"
	Selector2[2] = "ali haider"
	
	for y in range(len(Selector2)):
		Selector2[y] = Selector2[y].capitalize()

	return Selector1,Selector2





a = ['ali ahmed', 'ali zeshan','babar yonus','mk fe'] # this list should be of 12

b = ['Babar Younus', ' ali ahmed', 'kaka rival','asad afaq']

x = modify_players(a,b)
print(x)