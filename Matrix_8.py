#!/usr/bin/env python
# coding: utf-8

# # Documentation
# 
# 
# #### Infinite solution means that the polynomial has unreal roots (order is not equal to the degree)
# 
# ## CSV file entry rules:
# 
# #### The coefficients obtained using this code for a nth order polynomial would be the coefficients of terms from x^n to x, hence, the output/ dependent variable fed into the data should be of the form, 'x,f(x)-c' , where c is the constant term of the polynomial.
# 
# 
# #### Make sure to feed at least one such data entry that is not the root of the given polynomial, as this would avoid scaling issue.

# #defining back substitution

# In[8]:


def back_substitution(matrix, vector,n):
    x = [0] * n  
    for i in range(n - 1, -1, -1):  
        x[i] = vector[i] / matrix[i][i]  
        for j in range(i):
            vector[j] -= matrix[j][i] * x[i]
    return x


# #Importing Matrix

# In[9]:


import csv
A=[]
B=[]
row_A = int(input("Enter the order of the polynomial: "))
with open('data.csv','r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data = []
        for i in range(row_A+1):
            p = int(row[0])
            if p == 0 and i == 0 :
                data.append(1)
            else:
                data.append(p**i)
        A.append(data)
        B.append(int(row[1]))
print(A)
print(B)


# # Applying Gaussian Elimination

# In[10]:


for i in range(1,row_A):
    for j in range(i):
        list1 = [x * A[j][j] for x in A[i]]
        list2 = [x * A[i][j] for x in A[j]]
        B[i] = A[j][j]*B[i] - A[i][j]*B[j]
        A[i] = [x - y for x, y in zip(list1, list2)]
print("A = ",A ,"B = ",B)


# #Solving Equations using the matrices

# In[11]:


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
    solution.reverse()
    print("Solution:", solution)


# In[ ]:





# In[ ]:




