import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the matrix element(using space):")
a = np.array([list(map(int, input().split())) for _ in range(rows)])

print("\nMatrix:\n", a)

# Transpose
print("\nTranspose:\n", a.T)

# Determinant and Inverse (only for square matrices)
if rows == cols:
    print("\nDeterminant:", np.linalg.det(a))

    det = np.linalg.det(a)
    if det != 0:
        print("\nInverse:\n", np.linalg.inv(a))
    else:
        print("\nInverse does not exist (Determinant = 0)")
else:
    print("\nDeterminant and Inverse are only possible for square matrices.")

# Reshape
r = int(input("\nEnter new number of rows for reshape: "))
c = int(input("Enter new number of columns for reshape: "))

if r * c == rows * cols:
    print("\nReshaped Matrix:\n", a.reshape(r, c))
else:
    print("Reshape not possible. Number of elements must remain the same.")
