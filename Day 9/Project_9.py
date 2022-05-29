import os
import art

print(art.logo)
# Empty dictionary declaration
bidders = {}

another_bidder = "yes"
while another_bidder == "yes":
    print("Welcome to the secret auction program")
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    another_bidder = input("Are there any other bidders in the room? 'Yes' or 'No'\n").lower()
    os.system("cls")

highest_bidder_value = 0
highest_bidder_name = " "
for key in bidders:
    if bidders[key] > highest_bidder_value:
        highest_bidder_value = bidders[key]
        highest_bidder_name = key

print(f"The highest bidder is {highest_bidder_name} with a bid of ${highest_bidder_value}")
