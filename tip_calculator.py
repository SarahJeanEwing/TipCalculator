print("Welcome to the Tip Calculator!")
bill_total = input("What was the total bill? $")
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))/100
number_of_people = input("How many people to split the bill? ")
calculated_amount = (float(bill_total)*(1+tip_percentage) / int(number_of_people))
print(f"Each person should pay: ${calculated_amount:.2f}")