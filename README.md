# compound-interest-calculator
compound interest calculator
principle=0
rate=0
time=0
while principle<=0:
    principle=int(input("enter the amount:"))
    if principle<0:
        print("the principle should be positive")
    else:
        print(f"the amount is:${principle}")
while time<=0:
    time=int(input("enter the time:"))
    if time<0:
        print("ABORTING,Time cannot be negative.")
    else:
        print(f"the period alloted is:{time}years.")
while rate<=0:
    rate=float(input("enter the rate:"))
    if rate<0:
        print("ABORTING,Rate must be positive")
    else:
        print(f"the rate alloted by the bank is:{rate}")
if principle>=0 and time>0 and rate>0:
    final_amount=principle*((1+(rate/100))**(100*time))
else:
    print("the requirment was not accepted")
print("the program has ended")
    print(f"the final amount is:{final_amount}")
else:
    print("the requirment was not accepted")
