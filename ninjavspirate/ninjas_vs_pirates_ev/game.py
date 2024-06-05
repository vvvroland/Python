from classes.ninja import Ninja
from classes.pirate import Pirate
import random

#participants: Emily and Veronica 

michelangelo = Ninja("Michelanglo")
jack_sparrow = Pirate("Jack Sparrow")

print("Welcome to Pirates vs Ninjas! Choose your character: \n")

numPlayer= ""
multiplayer = False 

while numPlayer != "1" and numPlayer != "2":
    numPlayer = input("How many players? 1 or 2: \n")
    if (numPlayer == "1"):
        print("You have one player. Time to create your character! \n")
    
    elif (numPlayer == "2"):
        print("Multiplayer: Time to create your characters! \n")
        multiplayer = True

    else:
        print("Invalid number of players.\n")

character_type = ""
character_name = ""
player2_type = ""
player2_name = ""

while character_type != "p" and character_type != "n":
    character_type = input("Player 1, press 'p' for pirate and 'n' for ninja: \n")
    if (character_type == "p"):
        print(f"You are playing as a pirate, arrr!\n")

    elif (character_type == "n"):
        print(f"You are playing as a ninja. Shhh!\n")

    else: 
        print ("Not a valid choice. Try again!\n")

while character_name == "":
    if (character_type == "p"):
        character_name = input("What is your pirate's name?: \n")
        print(f"Your pirate's name is {character_name}\n")
        character = Pirate(character_name)
    
    else:
        character_name = input("What is your ninja's name?: \n")
        print(f"Your ninja's name is {character_name}\n")
        character = Ninja(character_name)

character.show_stats()


# MULTIPLAYER**********************************************
if multiplayer == True:
    while player2_type != "p" and player2_type != "n":
        print("Player Two, time to create your character!\n")
        player2_type = input("Press 'p' for pirate and 'n' for ninja: \n")
        if (player2_type == "p"):
            print(f"You are playing as a pirate, arrr!\n")

        elif (player2_type == "n"):
            print(f"You are playing as a ninja. Shhh!\n")

        else: 
            print ("Not a valid choice. Try again!\n")

        while player2_name == "":
            if (player2_type == "p"):
                player2_name= input("What is your pirate's name?: \n")
                print(f"Your pirate's name is {player2_name}\n")
                player2 = Pirate(player2_name)
            
            else:
                player2_name = input("What is your ninja's name?: \n")
                print(f"Your ninja's name is {player2_name}\n")
                player2 = Ninja(player2_name)

    player2.show_stats()
    print(f"{character.name} vs. {player2.name}: \tLet's get ready to rumble!!\n")

    while character.health > 0 and player2.health > 0:
        choice= ""
        print(f"{character.name}, it's your turn! {player2.name} has {player2.health} health. What will you do?:")
        
        while choice == "":
            choice = input("1) Attack \t 2) Heal: \n")
            
            if (choice == "1"):
                character.attack(player2)

            elif (choice == "2"):
                character.heal()
            
            else:
                print("Invalid choice. Try again!\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"It's {player2.name}'s turn! {character.name} has {character.health} health. What will you do?")

        choice2 = ""
        while choice2 == "":
            choice2 = input("1) Attack \t 2) Heal: \n")
            
            if (choice2 == "1"):
                player2.attack(character)

            elif (choice2 == "2"):
                player2.heal()
            
            else:
                print("Invalid choice. Try again!\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    if character.health <= 0:
        print(f"{player2.name} is the winner!")
    
    if player2.health <= 0:
        print(f"{character.name} is the winner!")

# ***********************************************************************
# SINGLEPLAYER
    
if multiplayer == False:
    roll = random.randint(1,10)
    
    if roll % 2 == 0:
        opponent = jack_sparrow
    elif roll % 2 != 0:
        opponent = michelangelo

    print(f"Your challenger is {opponent.name}. Prepare for battle!\n")
    opponent.show_stats()

    while character.health > 0 and opponent.health > 0:
        choice= ""
        print(f"What will you do?:")
        
        while choice == "":
            choice = input("1) Attack \t 2) Heal: \n")
            
            if (choice == "1"):
                character.attack(opponent)

            elif (choice == "2"):
                character.heal()
            
            else:
                print("Invalid choice. Try again!\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"It's {opponent.name}'s turn!\n")

        opponentChoice = random.randint(1,10)
        if opponentChoice % 2 == 0:
            opponent.attack(character)
        elif opponentChoice % 2 != 0:
            opponent.heal()

    if character.health <= 0:
        print(f"{opponent.name} is the winner!")
    
    if opponent.health <= 0:
        print(f"{character.name} is the winner!")
        