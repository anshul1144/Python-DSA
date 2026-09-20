# Program to print the right angled trinangle pattern of size n.
n=int(input("Enter the size of the triangle: "))

for i in range(1,n+1):
    for j in range (i):
        print("*",end=" ")
    print()