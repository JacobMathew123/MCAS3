import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the matrix:")
a = np.array([list(map(int, input().split())) for _ in range(rows)])

print("\nOriginal Matrix:\n", a)

print("\nRotate 90° Counterclockwise:")
print(np.rot90(a))

print("\nRotate 180°:")
print(np.rot90(a, 2))

print("\nRotate 270° Counterclockwise (or 90° Clockwise):")
print(np.rot90(a, 3))
