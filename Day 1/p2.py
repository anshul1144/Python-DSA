# Count the digit of the number.

num = int (input(" Enter the number : "))
count=0
n=num
# While loop for condition check
while n>0:
    last_digit=n%10  # modulus giver the remainder
    count=count+1
    n=n//10         # floor division gives quotient without decimal
print("The count of the digit is: ",count)
