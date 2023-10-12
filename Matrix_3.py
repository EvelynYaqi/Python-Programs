import numpy as np

# Input an nxm matrix using NumPy where 
#n is lenght of each matrix
#m is no of vectors
n = int(input("Length of each vector:"))
m = int(input("Number of vectors:"))
matrix = np.zeros((m, n), dtype=int)  # Create an nxm matrix filled with zeros

for i in range(m):
    for j in range(n):
       matrix[i, j] = int(input(f"Enter element at element {j + 1} of vector {i + 1}: "))
       print(i,j)
# Display the matrix
def projection(vec_A,vec_B):
	 

