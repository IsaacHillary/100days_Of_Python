print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
decision_1 = input("You arrive at a junction, would you like to go left or right?\n").lower()
if decision_1 == "left":
    decision_2 = input("You arrived at a small river, would you swim or wait?\n").lower()
    if decision_2 == "wait":
        decision_3 = input("You arrive in a room with 3 doors which will you choose; red, yellow, blue?\n").lower()
        if decision_3 == "yellow":
            print('''
                  {}
                 |__|
               ||    ||
              (_|    |_)
                 \  /
                  )(
                _|__|_
              _|______|_
             |__________|
            ''')
            print("You found the hidden treasures, You win!!!")
        elif decision_3 == "red":
            print("Burnt by fire, Game Over.")
        elif decision_3 == "blue":
            print("Eaten by beast, Game Over.")
        else:
            print("Game Over, Try again later.")
    else:
        print("Attacked by a crocodile, Game Over; Try Again Later.")
else:
    print("You fell into a hole, Game Over; Try Again Later.")