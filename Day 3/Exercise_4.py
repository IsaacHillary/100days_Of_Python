print("Welcome to Yummy-Hills Pizza Delivery service")
size = int(input("What size of pizza do you want? \n1. Small $15\n2. Medium $20\n3. Large $25\n"))
bill = 0
if size == 1:
    bill = 15
elif size == 2:
    bill = 20
elif size == 3:
    bill = 25

add_pepperoni = input("Do you want pepperoni added to your pizza? y/n \n")
if add_pepperoni == "y":
    if size == 1:
        bill += 2
    else:
        bill += 3

cheese = input("Do you want extra cheese? y/n \n")
if cheese == "y":
    bill += 1

print(f"Your total bill is ${bill}")
