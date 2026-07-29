# Program to check a number is divisible by two numbers.

num= int(input("Enter the number: "))
divisior1= int(input("Enter the divisior1:  "))
divisior2= int(input("Enter the divisior2 : "))

def Check_divisibility(num,divisior1,divisior2):
    if(num % divisior1==0 and num % divisior2==0):
        print("The number",num, "is divisible by both", divisior1, "and",divisior2)
    else:
        print("The number",num, "is not divisible by both ", divisior1, "and",divisior2)
        
Check_divisibility(num, divisior1 , divisior2)