# Input size of first matrix
r1 = int(input("Enter number of rows of Matrix A: "))
c1 = int(input("Enter number of columns of Matrix A: "))

# Input size of second matrix
r2 = int(input("Enter number of rows of Matrix B: "))
c2 = int(input("Enter number of columns of Matrix B: "))

# Check if multiplication is possible
if c1 != r2:
    print("Matrix multiplication is not possible.")
else:
    # Input Matrix A
    A = []
    print("Enter elements of Matrix A:")
    for i in range(r1):
        row = []
        for j in range(c1):
            element = int(input(f"A[{i}][{j}] = "))
            row.append(element)
        A.append(row)

    # Input Matrix B
    B = []
    print("Enter elements of Matrix B:")
    for i in range(r2):
        row = []
        for j in range(c2):
            element = int(input(f"B[{i}][{j}] = "))
            row.append(element)
        B.append(row)

    # Initialize result matrix with zeros
    result = []
    for i in range(r1):
        row = []
        for j in range(c2):
            row.append(0)
        result.append(row)

    # Matrix Multiplication
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]

    # Display Result
    print("\nProduct of the matrices:")
    for row in result:
        print(row)