import numpy as np
N = int(input("Enter the time period of the discrete signal (N):"))
x = [0]*N
for i in range (0,N):
    print("Enter X[",i+1,"]",end=' ')
    x[i] = int(input(":"))
k = int(input("Enter the position of the coeffecient:"))
ak=0
for i in range (0,N):
    ak = ak + x[i]*complex(np.cos(k*i*2*(np.pi)/N),np.sin(-k*i*2*(np.pi)/N))
print(ak/N)
