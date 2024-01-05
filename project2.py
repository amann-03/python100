print("Welcome to the Tip calculator\n")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10,12 or 15?"))
people = int(input("How many people to split the bill?"))

bill_with_tip = (tip/100)*bill + bill
bill_per_person = round(bill_with_tip / people,2) # round to 2 decimal places
bill_per_person = "{:.2f}".format(bill_per_person) # by this formatting it means after decimal there will be always 2 digits in floats

print(f"Each person should pay ${bill_per_person}.")
