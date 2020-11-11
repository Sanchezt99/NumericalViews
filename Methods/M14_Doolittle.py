def Doolittle(M, n):

	lower = [[0 for x in range(n)] 
				for y in range(n)]
	upper = [[0 for x in range(n)] 
				for y in range(n)]

	for i in range(n):
		for k in range(i, n): 
			sum = 0
			for j in range(i):
				sum += (lower[i][j] * upper[j][k])

			upper[i][k] = M[i][k] - sum

		for k in range(i, n):
			if (i == k):
				lower[i][i] = 1
			else:
				sum = 0
				for j in range(i):
					sum += (lower[k][j] * upper[j][i])
				lower[k][i] = int((M[k][i] - sum) /
									upper[i][i])

	print("		LT\t\t		UT")

	for i in range(n):
		
		# L
		for j in range(n):
			print(lower[i][j], end = "\t")
		print("", end = "\t")

		# U
		for j in range(n):
			print(upper[i][j], end = "\t")
		print("")

M = [[6, -1, -2],
	[-4, 1, 3],
	[-4, -2, 7]]

Doolittle(M, 3)

