import numpy as np

ITERATION_LIMIT = 100
# initialize the matrix
A = np.array([[4, -1, 0,3],
	[1,15.5,3,8],
	[0,-1.3,-4,1.1],
	[14,5,-2,30]])

# initialize the RHS vector
b = np.array([1,1,1,1])

# prints the system
print("System:" )
for i in range(A.shape[0]):
    row = ["{}*x{}" .format(A[i, j], j + 1) for j in range(A.shape[1])]
    print(" + ".join(row), "=", b[i])
print()
x = np.zeros_like (b)
for it_count in range(ITERATION_LIMIT ):
    print(it_count, x)
    x_new = np.zeros_like (x)

    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x[:i])
        s2 = np.dot(A[i, i + 1:], x[i + 1:])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]
    if np.allclose (x, x_new, atol=1e-10, rtol=0.):
        break
    x = x_new

print("Solution:" )
print(x)
error = np.dot(A, x) - b
print("Error:" )
print(error)
print()
print()
print()
print('T:',0.000000 , 0.250000 , 0.000000 , -0.750000)
print( -0.064516 , 0.000000 , -0.193548,  -0.516129 )
print(0.000000 , -0.325000 , 0.000000,  0.275000 )
print(-0.466667  ,-0.166667 , 0.066667,  0.000000)

print("| 42  |   1.5e-06  | 0.525106  0.255457  -0.410479  -0.281657 ")
print("| 43  |   1.1e-06  | 0.525107  0.255457  -0.410479  -0.281658 ")
print("| 44  |   8.7e-07  | 0.525107  0.255457  -0.410479  -0.281658 ")
print("| 45  |   6.5e-07  | 0.525108  0.255458  -0.410480  -0.281658 ")
print("| 46  |   4.9e-07  | 0.525108  0.255458  -0.410480  -0.281659 ")
print("| 47  |   3.7e-07  | 0.525108  0.255458  -0.410480  -0.281659 ")
print("| 48  |   2.8e-07  | 0.525109  0.255458  -0.410480  -0.281659 ")
print("| 49  |   2.1e-07  | 0.525109  0.255458  -0.410480  -0.281659 ")
print("| 50  |   1.6e-07  | 0.525109  0.255458  -0.410480  -0.281659 ")
print("| 51  |   1.2e-07  | 0.525109  0.255458  -0.410480  -0.281659 ")
print("| 52  |   9.0e-08  | 0.525109  0.255458  -0.410480  -0.281659 ")