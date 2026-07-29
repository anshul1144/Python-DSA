# Program to check if a given year is a leap year or not.

Year=int(input("Enter the year: "))
def Check_leap_year(Year):
    if ((Year % 400==0)|(Year % 4==0 and Year%100!=0)):
        print("Leap year")
    else:
        print("Not Leap Year")
        
Check_leap_year(Year)