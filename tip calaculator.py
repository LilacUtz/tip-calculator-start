print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
bill_float = float(bill)
tip_int = int(tip)
people_int = int(people)
tip_percent = tip_int / 100
tip_amount = bill_float * tip_percent
total_bill = bill_float + tip_amount
bill_per_person = total_bill / people_int
final_amount = round(bill_per_person, 2)
the_final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${the_final_amount}")
