def GaussSeidel(a, x ,b): 
	n = len(a)				 
	for j in range(0, n):		 
		temp = b[j]				 
		
		for i in range(0, n):	 
			if(j != i): 
				temp-=a[j][i] * x[i] 

		x[j] = temp / a[j][j] 
		 
	return x	 
	#implementar error		 
n = 4								 
				 
x = [0,0,0,0]						 
a = [[4, -1, 0,3],
	[1,15.5,3,8],
	[0,-1.3,-4,1.1],
	[14,5,-2,30]] 
b = [1,1,1,1] 
print(x) 


for i in range(0, 31):			 
	x = GaussSeidel(a, x, b) 
	print(i,x)					 
