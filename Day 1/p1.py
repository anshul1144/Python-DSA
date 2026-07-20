# Extraction of digit .

n=int(input("Enter a number: "))
num=n
digit=[]
while n>0:
    digit.append(n%10)
    n=n//10
print("Digits of the number are:", digit)