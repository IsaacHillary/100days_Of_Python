# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
first_number = str(name1.count("t")+name1.count("r")+name1.count("u")+name1.count("e")+name2.count("t") +
                   name2.count("r")+name2.count("u")+name2.count("e"))

second_number = str(name1.count("l")+name1.count("o")+name1.count("v")+name1.count("e")+name2.count("l") +
                    name2.count("o")+name2.count("v")+name2.count("e"))

love_score = first_number + second_number

if int(love_score) < 10 or int(love_score) > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif int(love_score) > 40 and int(love_score) < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
