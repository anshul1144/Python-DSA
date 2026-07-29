# Program to find the powsitive, negative and zero from the given number

num= int(input("Enter the number: "))
def check(num):
    if num > 0:
        return "The number is positive"
    elif num < 0:
        return "The number is negative"
    else:
        return "The number is zero."
    
print(check(num))