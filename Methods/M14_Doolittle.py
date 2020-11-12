#NOTE: NEED FIXES TO WORK AS INTENDED
import numpy as np
import sustprog as sus

def Doolittle(M, n):

	print('Stage 0')
	print(M)
	#size n*n
	LT = np.array([[0 for x in range(n)] 
				for y in range(n)])
	UT = np.array([[0 for x in range(n)] 
				for y in range(n)])

	#decomp
	for i in range(n):
		for k in range(i, n): 
			sum = 0
			for j in range(i):
				sum += (LT[i][j] * UT[j][k])

			UT[i][k] = M[i][k] - sum

		for k in range(i, n):
			if (i == k):
				LT[i][i] = 1
			else:
				sum = 0
				for j in range(i):
					sum += (LT[k][j] * UT[j][i])
				LT[k][i] = int((M[k][i] - sum) /
									UT[i][i])


	print('LT')
	print(LT)
		
	print('UT')
	print(UT)




M = np.array([[4, -1, 0,3],
	[1,15.5,3,8],
	[0,-1.3,-4,1.1],
	[14,5,-2,30]])

Doolittle(M, 4)

