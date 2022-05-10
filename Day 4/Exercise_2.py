import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#buyer = random.choice(names)
#print(f"{buyer} is going to buy the meal today!")

list_length = len(names)-1
buyer_index = random.randint(0, list_length)
buyer = names[buyer_index]
print(f"{buyer} is going to buy the meal today!")