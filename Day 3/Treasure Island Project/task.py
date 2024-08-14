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
 _________|___________| ;`-.o`"=._; ." ` '`." ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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

choice1 = input("You see a beautiful women on the road. "
                "Say Hi to her: 1 "
                "Get pass her: 2 ")
if choice1 == "1":
    print("She stabbed you with a knife and you died.")
else:
    choice2 = input("2 paths ahead. One leads to the jungle and other one leads to a river. "
                    "Type jungle or river: ").lower()
    if choice2 == "jungle":
        choice3 = input("You see something on the floor. "
                        "You can dig the spot with a shovel, throw a rock, get pass it. "
                        "Type shovel, rock or pass: ").lower()
        if choice3 == "shovel":
            print("A bomb exploded and you died.")
        elif choice3 == "rock":
            print("A bomb exploded and your leg chopped off. You died because of bleeding.")
        else:
            choice4 = input("Finally you see a treasure chest but a mouse sitting on top of it. "
                            "Type reason to try reason with her, "
                            "type kiss to kiss the mouse, "
                            "type yell to try scare the mouse, "
                            "type anything you want to say to her,\n"
                            "type attack to try attacking her: ").lower()
            if choice4 == "reason":
                print("It gets angry and eats you alive.")
            elif choice4 == "kiss":
                print("She turns to a fine lady and turns out "
                      "you have met your soulmate. You won.")
            elif choice4 == "yell":
                print("It gets angry and eats you alive.")
            elif choice4 == "attack":
                choice5 = input("Use your shovel or your fists. 1 or 2: ")
                if choice5 == "1":
                    print("You killed the mouse and took the treasure. You won.")
                else:
                    print("It was so fast. You couldn't even touch it before it ate you alive.")
            else:
                print("It didn't understand anything you say and ate you alive.")
    else:
        print("River was a diversion. A lion ate you alive.")
