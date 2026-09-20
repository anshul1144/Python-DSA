# Program to print the solid rectangle pattern of size n.
n=int(input(" ENter the size of the rectangle:"))

for i in range(n):
    for j in range (n+1):
        print("*",end=" ")

    print()