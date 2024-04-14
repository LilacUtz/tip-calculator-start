print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_percent = tip / 100
tip_amount = bill * tip_percent
total_bill = bill + tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
the_final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${the_final_amount}")
