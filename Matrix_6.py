#!/usr/bin/env python
# coding: utf-8

# #defining back substitution

# In[61]:


def back_substitution(matrix, vector,n):
    x = [0] * n  
    for i in range(n - 1, -1, -1):  
        x[i] = vector[i] / matrix[i][i]  
        for j in range(i):
            vector[j] -= matrix[j][i] * x[i]
    return x


# #Importing Matrix

# In[62]:


print("Format : Ax=B")
A=[]
row_A = col_A = int(input("Enter the dimension of input matrix:"))
for i in range(row_A):
    row = []
    for j in range(col_A):
        k = int(input(f"Value of A[{i+1},{j+1}] : "))
        row.append(k)
    A.append(row)
B=[]
for i in range(row_A):
    k = int(input(f"Value of B[{i+1},{1}] :"))
    B.append(k)
print(A)
print(B)


# #Applying Gaussian Elimination

# In[63]:


for i in range(1,row_A):
    for j in range(i):
        list1 = [x * A[j][j] for x in A[i]]
        list2 = [x * A[i][j] for x in A[j]]
        B[i] = A[j][j]*B[i] - A[i][j]*B[j]
        A[i] = [x - y for x, y in zip(list1, list2)]
print("A = ",A ,"B = ",B)


# #Solving Equations using the matrices

# In[64]:


C = []
blow = 0
for i in range(row_A):
    if A[i][i] == 0:
        if B[i] == 0:
            print("Infinite solutions")
            blow = 1
        else : 
            print("No solution")
            blow = 2
if blow == 0:
    solution = back_substitution(A, B, row_A)
    print("Solution:", solution)

