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