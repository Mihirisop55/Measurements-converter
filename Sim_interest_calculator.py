# Simple interest calculator
# i=(p*r*t)/100
# amount=i+p

p= 0
r= 0
t= 0

while p<=0:
    p= float(input("Enter the principal amount: "))
    if p<=0:
        print("Principal cannot be less than or equal to zero")
while r<=0:
    r= float(input("Enter the rate: "))
    if r<=0:
        print("Rate cannot be less than or equal to zero")
while t<=0:
    t= float(input("Enter the time in years: "))
    if t<=0:
        print("Time cannot be less than or equal to zero")

simple=(p*r*t)/100
amount= simple+p

print(f"The amount will be ${round(amount, 2)}")