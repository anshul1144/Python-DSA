# Program to take  an alphabet charector and check if it lies in between 'a' and 'm' or 'n' and 'z'
ch = input("Enter an alphabet character: ")

def check_alphabet(ch):
    if ch.isalpha() and len(ch) == 1:
        if 'a' <= ch <= 'm':
            return f"{ch} lies between 'a' and 'm'."
        elif 'n' <= ch <= 'z':
            return f"{ch} lies between 'n' and 'z'."
        else:
            return f"{ch} is not a lowercase alphabet character."
    else:
        return "Please enter a single alphabet character."
    
result = check_alphabet(ch)
print(result)