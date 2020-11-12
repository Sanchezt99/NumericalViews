def GaussSeidel(a, x ,b): 
	n = len(a)				 
	for j in range(0, n):		 
		temp = b[j]				 
		
		for i in range(0, n):	 
			if(j != i): 
				temp-=a[j][i] * x[i] 

		x[j] = temp / a[j][j] 
		 
	return x	 
				 
n = 3							
a = []							 
b = []		 
				 
x = [0, 0, 0]						 
a = [[6, 2, 1],[3, 7, 2],[6, 1, 3]] 
b = [3,2,7] 
print(x) 


for i in range(0, 25):			 
	x = GaussSeidel(a, x, b) 
	print(x)					 
