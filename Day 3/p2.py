# Program to take three input from the user and print the largest number.

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))

def largest_number(num1,num2,num3):
    if(num1>num2 and num1>num3):
        print("First number is greatest: ", num1)
    elif(num2>num3):
        print("Second number is greatest: ",num2)
    else:
        print("Third number is greatest: ",num3)
        
largest_number(num1,num2,num3)
