# 🚨 Don't change the code below 👇
print("WELCOME TO YOUR LEAP YEAR CALCULATOR")
y = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# This is how you work out whether if a particular year is a leap year.
# on every year that is evenly divisible by 4
# **except** every year that is evenly divisible by 100
# **unless** the year is also evenly divisible by 400

# Write your code below this line 👇

if y%4 == 0:
    if y%100 == 0:
        if y%400 == 0:
            print(f"{y} is a Leap Year.")
        else:
            print(f"{y} is not Leap Year.")
    else:
        print(f"{y} is a Leap Year.")
else:
    print(f"{y} is not Leap Year.")
    