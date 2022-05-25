print("This is a Prime Number Checker program")
# Prime Numbers are numbers only divisible by 1 and itself

# Write your code below this line 👇
def prime_checker(number):
    prime = True
    if number > 1:
        if number > 2:
            i = number - 1
            while prime is True and i > 1:
                if number % i == 0:
                    prime = False
                    print("It's not a prime number.")
                i -= 1
            if prime is True:
                print("It's a prime number.")
        else:
            print("It's a prime number.")
    else:
        print("It's not a prime number.")
# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
