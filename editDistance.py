def editDistance(inputtxt):
	transformationStep = []
	file = open(inputtxt)
	for i,line in enumerate(file):
		if i == 0:
			xSize = int(line)
			n = xSize + 1
		elif i == 1:
			x = line.rstrip()
		elif i == 2:
			ySize = int(line)
			m = ySize +1
		elif i == 3:
			y = line.rstrip()

	st = "*"+x		
	print("Oper    | c |Total| z")
	print("initial | 0 | 0   | "+st)
			
	cost = [[0 for i in range(xSize+1)] for j in range(ySize+1)]

	#setup matrice	
	for i in range (ySize+1):
		for j in range (xSize+1):

			if i == 0:
				cost[i][j] = j*3

			elif j == 0:
				cost[i][j] = i*2

			elif y[i-1] == x[j-1]:
				cost[i][j] = cost[i-1][j-1]

			else:
				cost[i][j] = min(cost[i][j-1]+3,	#Insert
								 cost[i-1][j]+2,		#Delete
								  cost[i-1][j-1]+4)	#Replace

	#print(cost[ySize][xSize])
	#backtrace
	operations = []
	total = 0
	while m > 1 or n > 1:
		if y[m-2] == x[n-2]:
			operations.append("left")
			m = m-1
			n = n-1
		else:
			Insert = cost[m-1][n-2]
			Delete = cost[m-2][n-1]
			Replace = cost[m-2][n-2]
			minimum = min(Insert,Delete,Replace)
			if minimum == Insert:
				operations.append("insert")
				n = n-1
			elif minimum == Delete:
				operations.append("delete")
				m = m-1
			elif minimum == Replace:
				operations.append("replace")
				m = m-1
				n = n-1
			else:
				print("should not happen")

	ops = operations[::-1]
	#print(ops)
	countX = 0
	countY = 0

	for i in ops:
		if i == "left": 
			countX = countX + 1
			countY = countY + 1
			newX = x[:countX] + '*' + x[countX:]
			print("right   | 0 | "+str(total)+"   | "+newX)

		elif i == "insert":
			getY = y[countY]
			newX = x[:countX] + getY + '*' + x[countX:]
			x = x[:countX] + getY + x[countX:]
			countX = countX + 1
			countY = countY + 1
			total = total + 3
			print("insert  | 3 | " + str(total) + "   | "+newX )
			m = m - 1
		elif i == "delete":
			newX = x[:countX] + '*' + x[countX+1:]
			x = x[:countX]+x[countX+1:]
			total = total + 2
			print("delete  | 2 | " + str(total) + "   | "+newX )
			n = n - 1
		elif i == "replace":
			getY = y[countY]
			newX = x[:countX] + getY + '*' + x[countX+1:]
			x = x[:countX]+getY+x[countX+1:]
			countY = countY + 1
			countX = countX + 1
			total = total + 4
			print("replace | 4 | " + str(total) + "   | "+ newX )
			m = m - 1 
			n = n - 1
		else:
			print("error")



editDistance('sample.txt')