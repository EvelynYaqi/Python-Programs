def norm(a,b,c):
	result = ((a**2)+(b**2)+(c**2))**(0.5)
	return result
print("Enter the components of the vector")
a = [0,0,0,0]
a[0]= int(input("Enter n3x component:"))
a[1]= int(input("Enter n3y component:"))
a[2]= int(input("Enter n3z component:"))
a[3]= int(input("Enter c_3 :"))
norm_n3 = norm(a[0],a[1],a[2])
b = [0,0,0,0]
b[0]= int(input("Enter n2x component:"))
b[1]= int(input("Enter n2y component:"))
b[2]= int(input("Enter n2z component:"))
b[3]= int(input("Enter c_2 :"))
norm_n2 = norm(b[0],b[1],b[2])
soln_vec = [0,0,0,0]
i=0
for i in range(0,4):
	soln_vec[i] = ( (a[i] / norm_n3)-(b[i] / norm_n2))
	i=i+1
print("(",soln_vec[0],"    ",soln_vec[1],"    ",soln_vec[2],").x = ", soln_vec[3])
