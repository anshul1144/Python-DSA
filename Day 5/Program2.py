# Program to print the solid square pattern of size n.
n= int (input("Enter the size of the square: "))

for i in range(n):
    for j in range (n):
        print("*", end=" ")
    print()