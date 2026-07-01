# compound interest calculator
# A=P(1+(R/N)**T)  (N=100)

principle=0
rate= 0
time= 0

while principle<=0:
    principle = float(input("Enter the principle: "))
    if principle<=0:
         print("Principle can't be less than or equal to zero")
while rate<=0:
    rate = float(input("Enter the rate: "))
    if rate<=0:
        print("Interest can't be less than or equal to zero")
while time <= 0:
    time = int(input("Enter the time in years: "))
    if time<=0:
        print("Time can't be less than or equal to zero")

amount = principle * (1+(rate/100))**time

print(f"The amount is ${round(amount, 2)}")