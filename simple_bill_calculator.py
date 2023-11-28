print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage of tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split bill? "))

payment = round((bill+(tip*bill/100))/ no_of_people , 2)

print(f"Each person should pay: ${payment}")
