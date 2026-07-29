# Program to take temperature value and print "cold", "warm", "Hot" using range condition.

Temperature=int(input("Enter the temperature in degree celcius : "))

def check_temperature(Temperature):
    if(Temperature<20):
        print("Today is cold: ",Temperature)
    elif(20<Temperature<35):
        print("Today is warm: ",Temperature)
    else:
        print("TOday is hot: ",Temperature)
        
check_temperature(Temperature)
