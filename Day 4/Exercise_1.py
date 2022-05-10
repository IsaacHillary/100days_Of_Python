# Coin Toss Progam
import random
print("Welcome to a coin toss game")
choice = int(input('Press "1" for Head and "0" for Tail\n'))
random_coin = random.randint(0,1)

if random_coin == 1 and choice == 1:
    print("   Head\nHooray, You Win.")
elif random_coin == 0 and choice == 0:
    print("   Tail\nHooray, You Win.")
else:
    print(f"Sorry you lost, The Answer was {random_coin}. Try again later. ")