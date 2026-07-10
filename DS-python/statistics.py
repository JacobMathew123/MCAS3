import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the matrix:")
a = np.array([list(map(int, input().split())) for _ in range(rows)])

print("\nMatrix:\n", a)

print("\nSum =", np.sum(a))
print("Mean =", np.mean(a))
print("Maximum =", np.max(a))
print("Minimum =", np.min(a))