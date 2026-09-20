# Program to print hollow square pattern of size n.
n = int(input("Enter the size of square: "))

for i in range(n):
    for j in range(n):
        # First/last row ya first/last column par * print hoga
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()