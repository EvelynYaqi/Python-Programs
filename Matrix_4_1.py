#!/usr/bin/env python
# coding: utf-8

# # Creating a random matrix , compressing it to CSR and then regenerating it

# ##Creating a random matrix

# In[44]:


import random as rand
choices = [0,1,2,3,4,5]
weights = [0.4,0.15,0.15,0.1,0.1,0.1]
def dice():
	dice = (rand.choices(choices, weights))         
	return dice
n = int(input("Enter the dimension of the matrix:"))
matrix = []
for i in range(n):
    row = []  
    for j in range(n):
        row.append(dice())  # Fill the row with values
    matrix.append(row)  # Add the row to the matrix
print(matrix)


# ##Compressing the matrix to CSR format

# In[45]:


value = []
col_ind = []
row_ind = []
N = 0
for i in range(n):
    row_ind.append(len(value))
    for j in range(n):
        if matrix[i][j][0] != 0:
            value.append(matrix[i][j][0])
            col_ind.append(j)
            N = N+1
print("value:",value,"\n","col_ind:",col_ind,"\n","row_ind:",row_ind)
        


# ##Regenarting matrix using CSR

# In[46]:


reg_matrix = [[0] * n for _ in range(n)]


# In[47]:


row = 0
col = 0
for i in range(n-1):
    if row_ind[i] != row_ind[i+1]:
        for j in range(row_ind[i],row_ind[i+1]):
            reg_matrix[i][col_ind[j]] = value[j]
for i in range(row_ind[n-1],N):
    reg_matrix[n-1][col_ind[i]] = value[i]
print(reg_matrix)


# ##Generating a random vector of length n

# In[48]:


choices = [0,1,2,3,4,5,6,7,8,9]
weights = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
def dice_roll():
	dice = (rand.choices(choices, weights))         
	return dice
vector = []
for i in range(n):
    vector.append(dice_roll())
print(vector)


# ##Multiplying matrix with a vector using CSR outputs

# In[49]:


product_matrix = []
for i in range(n-1):
    p = 0
    if row_ind[i] != row_ind[i+1]:
        for j in range(row_ind[i],row_ind[i+1]):
            p = p + vector[col_ind[j]][0]*value[j]
    product_matrix.append(p)
p=0
for i in range(row_ind[n-1],N):
    p = p + vector[col_ind[i]][0]*value[i]
product_matrix.append(p)
print(product_matrix)


# In[ ]:





# In[ ]:




