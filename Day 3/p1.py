# Program to take two numbers and find the largest one.

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

def largest_number(num1,num2):
    if(num1>num2):
        print("First number is the greatest:",num1)
        
    else:
        print("Second number is the greatest:",num2)
        
largest_number(num1,num2)