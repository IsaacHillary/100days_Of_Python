rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
print("This is a Rock, Paper and Scissor game")
images = [rock, paper, scissors]
user_choice = int(input('What\'s your choice? "0" for Rock, "1" for Paper or "2" for Scissor.\n'))
computer_choice = random.randint(0, 2)

if user_choice <= 2 and user_choice >= 0:

    print(images[user_choice])
    print("Computer Chose:")
    print(images[computer_choice])

    # Game rules implementation
    if user_choice == 2 and computer_choice == 1:
        print("You Win")
    elif user_choice == 1 and computer_choice == 0:
        print("You Win")
    elif user_choice == computer_choice:
        print("It's a Draw")
    elif user_choice == 0 and computer_choice == 2:
        print("You Win")
    else:
        print("You Lose")
else:
    print("Invalid number, you lose")
