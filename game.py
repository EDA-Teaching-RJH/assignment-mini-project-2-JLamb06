import re
import cowsay
import random
urweapons = []
inventory = []
equipped = []
turns = 0

class Character:
    types = ["knight","wizard","archer"]
    avaiweapons = ["sword","shield","spear","wand","staff","barebow","recurvebow"]
    

    def __init__ (self,name,weapon,type):
        global types
        global avaiweapons
        self.name = name
        self.weapon = weapon
        self.type = type

    def main(self):
        character = self.get_character()
        print(cowsay.beavis(f"I am {character.name} a {character.type} with a {character.weapon}"))

    def get_character(self):
        name = input("Enter your characters name: ")
        typeyn = False
        while typeyn == False:
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
                weapon = self.avaiweapons[5]
                urweapons.append(weapon)
                equipped.append(weapon)
                break
            else:
                print("That is not a valid class, please try again.")
        
        character = Character(name,weapon,type)
        return character

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

if __name__ == "__main__":
    character = Character("", "","")
    character.main()

def fox():
    global turns
    while foxstats["Health"] > 0 and urstats["Health"] > 0:
        turns += 1
        if turns == 2:
            print(cowsay.fox(f"I am going to teach you how to play \n I have {foxstats['Health']} health and you must roll a higher \n number than I do to be able to hit me. "))
        else:
            print(cowsay.fox(f"I am going to defeat you!!! \n I have {foxstats['Health']} health. "))
        attack = input("Would you like to attack or escape? ")
        ur_dice_roll()
        game_dice_roll()
        attack = attack.lower().strip()
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
                    print(cowsay.stego(f"Noooo, I have been Defeated \n You now get {stegostats['Points']} points."))
                    turns = turns + 1
                else:
                    print(cowsay.stego(f"Ouch, I now have {stegostats["Health"]} health left."))
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
    turns += 1
    enemies = ["fox","stego"]
    enemy = "fox"
    plays = True
    plays1 = "yes"
    if turns > 1:
        while plays == True:
            plays1 = input ("Would you like to continue playing? \nPlease enter yes or no. ")
            plays1 == plays1.strip().lower()
        enemy = random.choice(enemies)
    while plays1 == "yes":
        if enemy == "fox":
            fox()
            if plays1 == "no" or urstats["Health"] <= 0:
                savedscore = True
                while savedscore == True:
                    savescore = input("Would you like to save your score? \n Please enter yes or no. ")
                    savescore = savescore.strip().lower()
                    if savescore == "yes":
                        code = input("Enter a 6 digit numerical code to remember your score.")
                        if re.search (r"[6Z0-9]", code):
                            scoresheet = open("Scoresheet.txt", "a")
                            scoresheet.write (f"Code: {code}, Name: {character.name} with {urstats['points']} points. \n")
                        else:
                            raise ValueError("That is not a valid code so your progress will not be saved.")
                    else:
                        cowsay.beavis(f"Our hard work will not be remembered.")
                scoredboard = True
                while scoredboard == True:
                    scoreboard = input("Would you like to see one of your previous scores? If so please enter yes or no. ")
                    scoreboard = scoreboard.strip().lower()
                    if scoreboard == "yes":
                        code2 = input("Enter the 6 digit numerical code you used. ")
                        with open(r'Scoresheet.txt', 'r') as file:
                            scores = file.readline(code2)
                            if code2 in scores:
                                print(scores.code2)
                            else:
                                print("A character with that code does not exist. ")
                    if scoreboard == "no":
                        print("Thanks for playing.")
        if enemy == "stego":
            stegosaurus()
            if plays1 == "no" or urstats["Health"] <= 0:
                savedscore = True
                while savedscore == True:
                    savescore = input("Would you like to save your score? \n Please enter yes or no. ")
                    savescore = savescore.strip().lower()
                    if savescore == "yes":
                        code = input("Enter a 6 digit numerical code to remember your score.")
                        if re.search (r"[6Z0-9]", code):
                            scoresheet = open("Scoresheet.txt", "a")
                            scoresheet.write (f"Code: {code}, Name: {character.name} with {urstats['points']} points. \n")
                    else:
                        raise ValueError("That is not a valid code so your progress will not be saved.")
                else:
                    cowsay.beavis(f"Our hard work will not be remembered.")
                scoredboard = True
                while scoredboard == True:
                    scoreboard = input("Would you like to see one of your previous scores? If so please enter yes or no. ")
                    scoreboard = scoreboard.strip().lower()
                    if scoreboard == "yes":
                        code2 = input("Enter the 6 digit numerical code you used. ")
                        with open(r'Scoresheet.txt', 'r') as file:
                            scores = file.readline(code2)
                            if code2 in scores:
                                print(scores.code2)
                            else:
                                print("A character with that code does not exist. ")
                    if scoreboard == "no":
                        print("Thanks for playing.")
    
        
game()
