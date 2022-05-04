# Day 2 Project TIP CALCULATOR
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?  $"))
percentage = (float(input("What is the tip bill percentage?  ")) / 100)
people = float(input("How many people to split the bill?  "))

# Adding the percentage of the bill to the initial bill
_bill = total_bill * percentage
total_bill = total_bill + _bill

# Spliting the bill between number of persons
# each_pay = round(total_bill/people, 2)
each_pay = "{:.2f}".format(total_bill/people)
print(f"Each person should pay: ${each_pay}")
