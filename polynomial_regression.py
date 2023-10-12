import matplotlib.pyplot as plt

# To multiply two matrices
def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

# To compute solution of the equation Ax = b. 
def gauss_elimination(A, b):
    # It returns None if the input is invalid, and returns x = 0 the number of solutions is zero/infinite.
    rows = len(A)
    columns = len(A[0])

    # Error condition
    if(len(b) != rows):
        print("Invalid Input. Number of columns of A must be equal to number of rows of b. ")
        return None

    # Forward Elimination Phase
    for i in range(0,columns):
        for j in range(i+1, rows):
            b[j][0] = A[i][i]*b[j][0] - A[j][i]*b[i][0]
            A[j] = [x - y for x, y in zip([z * A[i][i] for z in A[j]], [z * A[j][i] for z in A[i]])]

    # Checking for linear dependency, and presence of zero/infinite solutions (through flag)
    ld = False
    flag = False
    for i in range(0,rows):
        if(A[i] == [0]*columns):
            ld = True
            if(b[i]!=0):
                flag = True

    # No Solutions Case
    if(flag == True and ld == True):
        print("No Solutions")
        return 0

    # Infinite Solutions Case
    elif(flag == False and ld == True and rows<=columns):
        print("Infinite Solutions")
        return 0
    
    # If the system is overdetermined yet a solution exists (due to linear dependency of two or more equations)
    elif(flag == False and ld == True and rows>columns):
        for i in range(0,rows):
            if(A[i] == [0]*columns):
                A.pop(i)
                b.pop(i)
                rows -= 1

    # Backward Substitution
    x = [0]*columns
    for i in reversed(range(0, rows)):
        sum = 0
        for j in range(i+1,columns):
            sum += A[i][j]*x[j]
        x[i] = (b[i][0] - sum)/A[i][i]  

    return x

# To generate the regression matrices
def polynomial_regression(faddress, order):
    # Regression Matrices - Matrix y is the matrix of outputs and matrix A is the matrix of features (which are 1, x, x^2, x^3, etc)
    A = []
    y = []

    # Filling matrices
    f = open(faddress, "r")
    for row in f:
        # Converting to numbers
        strx, stry = row.split(',')
        strx = strx.strip()
        stry = stry.strip()
        try:
            y.append([float(stry)])
            A.append([float(strx)**n for n in range(0,order+1)])
        except:
            continue
    f.close()
    
    A_T = [[row[m] for row in A] for m in range(len(A[0]))]

    # Performing Gaussian Elimination to determine coefficients
    return gauss_elimination(matmul(A_T, A), matmul(A_T, y))

def out(x, coeffs):
    # To return the output of the polynomial which has been deduced in the regression problem. 
    y = [0]*len(x)
    for i in range(0, len(coeffs)):
        for j in range(0, len(x)):
            y[j] += (x[j]**i)*coeffs[i]
    return y

def plot(faddress, coeffs):
    f = open(faddress, "r")
    y = []
    x = []
    for row in f:
        # Converting to numbers
        strx, stry = row.split(',')
        strx = strx.strip()
        stry = stry.strip()
        try:
            y_curr = float(stry)
            x_curr = float(strx)
            y.append(y_curr)
            x.append(x_curr)
        except:
            continue
    f.close()

    # Output of regression function
    reg = out(x, coeffs)

    # Plotting 
    plt.scatter(x, y, label = "Input Values", color = 'r', marker='x')
    plt.plot(x, reg, label = "Best-fit polynomial", color = 'b')
    plt.xlabel("Input (x)")
    plt.ylabel("Output (y)")
    plt.title("Polynomial Regression")
    plt.legend()
    plt.show()

#########################
# Give your inputs here #
#########################

# Give the address of your file here - it must be a csv file with each row having the independent variable followed by the dependent variable. The order of the polynomial must be less than or equal to the number of input cases in the csv file.
# Format (Windows): 
# faddress = f"C:/Users/hp/Desktop/Coding/EE23000 - Matrix Theory/Polynomial_Regression/Data.csv"
faddress = f"C:/Users/hp/Desktop/Coding/EE23000 - Matrix Theory/Polynomial_Regression/DataNew.csv"

# Give the order of the polynomial here
order = 4

# Coefficients and plotting
coeffs = polynomial_regression(faddress, order)

print("Best-fit Polynomial: ")
for i in reversed(range(len(coeffs))):
    if(i>=2):
        print(f"{coeffs[i]} x^{i} + ")
    if(i==1):
        print(f"{coeffs[i]} x +")
    if(i==0):
        print(f"{coeffs[i]} ")

plot(faddress, coeffs)