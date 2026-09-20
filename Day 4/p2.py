"""Take a 3-digit number and determine if the middle digit is the largest, smallest, or neither .
n = 123
num = n
seen = set()

while num > 0:
    digit = num % 10
    if digit in seen:
        print("number is not distinct")
        break
    seen.add(digit)
    num //= 10
else:
    print("number is distinct")
    like that, you can check if the middle digit is the largest, smallest, or neither by extracting the digits and comparing them. Here's an example code snippet to achieve that:
    """
n = 123  # Example 3-digit number

