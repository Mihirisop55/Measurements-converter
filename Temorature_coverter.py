# Fahrenheit to Celsius Formula:
# C° = ((°F - 32)*5) / 9
# Celsius to Fahrenheit Formula:
#°F = (°C * 1.8) + 32



temp=float(input("Enter the temprature: "))
unit=input("Enter the unit of temprature (C/F):").lower()
if unit!="c" and unit!="f":
    print("Enter a valid unit")
else:
    if unit=="c":
        print(f"The temprature in fahrenheit is {round(((temp * 1.8) + 32),2)}")
    elif unit=="f":
        print(f"The temorature in celsius is {round((((temp - 32)*5) / 9),2)}")