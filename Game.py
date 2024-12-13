#imports the required libraries
import re
import cowsay
import random
#sets the required lists
urweapons = []
inventory = []
equipped = []
turns = 0
#creates a class called character
class Character:
    types = ["knight","wizard","archer"]
    avaiweapons = ["sword","shield","spear","wand","staff","barebow","recurvebow"]

    def __init__ (self,name,weapon,type):
        #makes the variables global(available anywhere in the code)
        global types
        global avaiweapons
        self.name = name
        self.weapon = weapon
        self.type = type

    def main(self):
        global character
        character = self.get_character()
        #prints out the 3 parts of the class
        print(cowsay.beavis(f"I am {character.name} a {character.type} with a {character.weapon}"))

    def get_character(self):
        #recieves the input for name
        name = input("Enter your characters name: ")
        typeyn = False
        while typeyn == False:
            #recieves the input for type
            type = input(f"Enter you character type from the list {self.types}: ")
            type = type.lower().strip()
            if type == "knight":
                weapon = self.avaiweapons[0]
                urweapons.append(weapon)
                break
            if type == "wizard":
                weapon = self.avaiweapons[3]
                urweapons.append(weapon)
                break
            if type == "archer":
                #assigns the weapon
                weapon = self.avaiweapons[5]
                #adds the weapon to the desired list
                urweapons.append(weapon)
                equipped.append(weapon)
                #ends the while loop
                break
            else:
                #Will print this if there is an error
                print("That is not a valid class, please try again.")
        #takes the class and assigns it to a list so the variables can be accessed
        character = Character(name,weapon,type)
        return character
#Creates a dice roller for the player and the game
def ur_dice_roll():
    global roll
    roll = random.randint(1,6)

    if roll == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    if roll == 2:
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
    if roll == 3:
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
    if roll == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    if roll == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    if roll == 6:
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")

def game_dice_roll():
    global gameroll
    gameroll = random.randint(1,6)

    if gameroll == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    if gameroll == 2:
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
    if gameroll == 3:
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
    if gameroll == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    if gameroll == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    if gameroll == 6:
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")
#Creates dictionaries for all the stats and parts that may vary or be required
Barebow = {
    "Damage" : 25,
    "Armour" : "Piercing"
}

Sword = {
    "Damage" : 10,
    "Armour" : "Blunt"
}

Wand = {
    "Damage" : 20,
    "Armour" : "Stun"
}

urstats = {
    "Health" : 150,
    "Armour" : 1,
    "money" : 0,
    "points" : 0,
}

foxstats = {
    "Health" : 50,
    "Damage" : 10,
    "Armour" : 1,
    "Points" : 15
    }

stegostats = {
    "Health" : 200,
    "Armour" : 20,
    "Points" : 200,
    "Damage" : 75
}

attacks = ["attack","escape"]
#Allows the character class to function and be accessed
if __name__ == "__main__":
    character = Character("", "","")
    character.main()
#defines all the functions the fox can do
def fox():
    global turns
    while foxstats["Health"] > 0 and urstats["Health"] > 0:
        turns += 1
        if turns == 2:
            #uses the cowsay library to show and tell the user what the character is saying
            print(cowsay.fox(f"I am going to teach you how to play \n I have {foxstats['Health']} health and you must roll a higher \n number than I do to be able to hit me. "))
        else:
            print(cowsay.fox(f"I am going to defeat you!!! \n I have {foxstats['Health']} health. "))
        attack = input("Would you like to attack or escape? ")
        ur_dice_roll()
        game_dice_roll()
        attack = attack.lower().strip()
        #access the global variables from the other definitions and uses them
        if attack == "attack" and roll > gameroll:
            if "barebow" in equipped:
                foxstats["Health"] = foxstats["Health"] - Barebow["Damage"]
                if foxstats["Health"] <= 0:
                    print(cowsay.fox(f"Noooo, I have been Defeated \n You now get {foxstats['Points']} points."))
                    turns =+ 1
                else:
                    print(cowsay.fox(f"Ouch, I now have {foxstats["Health"]} health left."))
            if "sword" in equipped:
                foxstats["Health"] = foxstats["Health"] - Sword["Damage"]
                if foxstats["Health"] <= 0:
                    print(cowsay.fox(f"Noooo, I have been Defeated \n You now get {foxstats['Points']} points."))
                    turns =+ 1
                else:
                    print(cowsay.fox(f"Ouch, I now have {foxstats["Health"]} health left."))
            if "wand" in equipped:
                foxstats["Health"] = foxstats["Health"] - Wand["Damage"]
                if foxstats["Health"] <= 0:
                    print(cowsay.fox(f"Noooo, I have been Defeated \n You now get {foxstats['Points']} points."))
                    turns =+ 1
                else:
                    print(cowsay.fox(f"Ouch, I now have {foxstats["Health"]} health left."))
        if attack == "escape" and roll > gameroll:
            print(cowsay.beavis(f"Runaway!!!! \n I escaped with {urstats["Health"]} health"))
            break
        if attack == "escape" and roll < gameroll:
            print(cowsay.beavis(F"I can't escape at the moment"))
        if gameroll > roll:
            if "shield" in equipped:
                urstats["Health"] = urstats["Health"] - (foxstats["Damage"] / 10)
                if urstats["Health"] <= 0:
                    urstats["Health"] = 0
                    print(cowsay.beavis(f"Aaargh, I've been defeated!!!! \n You got {urstats['points']} points before dying. "))
                    turns =+ 1
                else:
                    print(cowsay.beavis(f"Ouch you just hit me! \n I now have {urstats['Health']}"))
            else:
                urstats["Health"] = urstats["Health"] - foxstats["Damage"]
                print(cowsay.beavis(f"Ouch you just hit me! \n I now have {urstats['Health']}"))
        if roll == gameroll:
            print(cowsay.beavis(f"We'll call this one a draw. "))
        if attack not in attacks:
            print ("Please enter a valid response.")
#Same as fox() but with different stats and stegosaurus instead of fox
def stegosaurus():
    while stegostats["Health"] > 0 and urstats["Health"] > 0:
        print(cowsay.stegosaurus(f"I am going to defeat you!!! \n I have {stegostats['Health']} health. "))
        attack = input("Would you like to attack or escape? ")
        ur_dice_roll()
        game_dice_roll()
        attack = attack.lower().strip()
        if attack == "attack" and roll > gameroll:
            if "barebow" in equipped:
                stegostats["Health"] = stegostats["Health"] - Barebow["Damage"]
                if stegostats["Health"] <= 0:
                    print(cowsay.stegosaurus(f"Noooo, I have been Defeated \n You now get {stegostats['Points']} points."))
                    turns = turns + 1
                else:
                    print(cowsay.stegosaurus(f"Ouch, I now have {stegostats["Health"]} health left."))
            if "sword" in equipped:
                stegostats["Health"] = stegostats["Health"] - Sword["Damage"]
                if stegostats["Health"] <= 0:
                    print(cowsay.stegosaurus(f"Noooo, I have been Defeated \n You now get {stegostats['Points']} points."))
                    turns =+ 1
                else:
                    print(cowsay.stegosaurus(f"Ouch, I now have {stegostats["Health"]} health left."))
            if "wand" in equipped:
                stegostats["Health"] = stegostats["Health"] - Wand["Damage"]
                if stegostats["Health"] <= 0:
                    stegostats["Health"] = 0
                    print(cowsay.stegosaurus(f"Noooo, I have been Defeated \n You now get {stegostats['Points']} points."))
                    turns =+ 1
                else:
                    print(cowsay.stegosaurus(f"Ouch, I now have {stegostats["Health"]} health left."))
        if attack == "escape" and roll > gameroll:
            print(cowsay.beavis(f"Runaway!!!! \n I escaped with {urstats["Health"]} health"))
            break
        if attack == "escape" and roll < gameroll:
            print(cowsay.beavis(F"I can't escape at the moment"))
        if gameroll > roll:
            if "shield" in equipped:
                urstats["Health"] = urstats["Health"] - (foxstats["Damage"] / 10)
                if urstats["Health"] <= 0:
                    urstats["Health"] = 0
                    print(cowsay.beavis(f"Aaargh, I've been defeated!!!! \n You got {urstats['points']} points before dying. "))
                    turns = turns + 1
                else:
                    print(cowsay.beavis(f"Ouch you just hit me! \n I now have {urstats['Health']}"))
            else:
                urstats["Health"] = urstats["Health"] - stegostats["Damage"]
                print(cowsay.beavis(f"Ouch you just hit me! \n I now have {urstats['Health']}"))
        if roll == gameroll:
            print(cowsay.beavis(f"We'll call this one a draw. "))
        if attack not in attacks:
            print ("Please enter a valid response.")


def game():
    global turns
    global eroor
    eroor = ""
    turns += 1
    fox()
    stegosaurus()
    savescore = input("Would you like to save your score? \nPlease enter yes or no. ")
    savescore = savescore.strip().lower()
    if savescore == "yes":
        code = input("Enter a 6 digit numerical code to remember your score. ")
        #Uses regex to check that the code given is only 6 characters long and all are numbers
        if re.search (r"^[0-9]{6,6}$", code):
            #opens the file
            #and appends the score name and code to the scoresheet
            scoresheet = open("Scoresheet.txt", "a")
            scoresheet.write (f"Code: {code}, Name: {character.name} with {urstats['points']} points.\n")
            print("Added your score to the scoreboard")
            scoresheet.close()
            #closes the file
        else:
            #Will print this if an error is produced
            raise ValueError("That is not a valid code so your progress will not be saved. ")
    else:
        cowsay.beavis(f"Our hard work will not be remembered.")
    
    scoreboard = input("Would you like to see one of your previous scores? If so please enter yes or no. ")
    scoreboard = scoreboard.strip().lower()
    if scoreboard == "yes":
        code2 = input("Enter a numerical code to access the scoreboard ")
        try:
            if re.search (r"^[0-9]{6,6}$", code2):
                #opens the file
                #Reads the file
                file = open("Scoresheet.txt","r")
                #Prints all the lines in the text file. 
                for x in file:
                    print(x)
            else:
                eroor = ValueError
        except:
            eroor = ValueError
    if scoreboard == "no":
        print("Thanks for playing.")

def complete():
    game()
    #will print these parts if a value occured 
    if eroor == ValueError:
        print("That is an invalid input")
    if eroor == ZeroDivisionError:
        print("You cannot divide by 0")
    else:
        #if no error occured then it will just print thanks
        print("Thanks for playing")

complete()