print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $ "))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

pay = (bill + (bill * tip / 100)) / people

print(F"Each person should pay: {round(pay, 2)}")
