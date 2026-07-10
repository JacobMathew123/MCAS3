import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the matrix:")
a = np.array([list(map(int, input().split())) for _ in range(rows)])

print("\nOriginal Matrix:\n", a)

print("\nFlip Up-Down (Vertical):")
print(np.flipud(a))

print("\nFlip Left-Right (Horizontal):")
print(np.fliplr(a))

print("\nFlip Both Rows and Columns:")
print(np.flip(a))
