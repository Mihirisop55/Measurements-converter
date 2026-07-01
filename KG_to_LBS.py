# Calculator
# kg to lbs
# lbs to kg

unit1= input("Enter your measuring unit(KG/LBS): ").lower()
unit2= input("Enter the unit you want to convert(KG/LBS): ").lower()

if unit1 == unit2:
    print("The units are same")
else:
    mass=int(input("Enter your mass: "))
    if unit1=="kg":
        print(f"Your mass in LBS is {round((mass*2.20462),2)} lbs")
    elif unit1=="lbs":
        print(f"Your mass in KG is {round((mass*0.45359237),2)} kg")
    else:
        print("An error occured")