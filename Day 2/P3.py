# Program to check that the given number is divisible by another number or not.

# Get user input for the number and the divisor
num=int(input("Enter the number: "))
divisor=int(input("Enter the divisor: "))

#define a function to check divisibility
def check_divisibility(num, divisor):
    if num % divisor == 0:
        print(f"{num} is divisible by {divisor}.")
    else:
        print(f"{num} is not divisible by {divisor}.")

# Call the function to check divisibility 
check_divisibility(num, divisor)