# Program to print the hollow rectangle pattern of size n.

n= int(input("Enter the size of the rectangle:"))

for i in range(n):
    for j in range(n+1):
        if i==0 or i==n-1 or j==0 or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()