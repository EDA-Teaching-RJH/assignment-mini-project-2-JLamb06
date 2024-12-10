import re
import cowsay
import random
urweapons = []
inventory = []
equipped = []

class Character:
    types = ["knight","wizard","archer"]
    avaiweapons = ["Sword","Shield","2 Handed Sword","2 Swords","Spear","Wand","Staff","Magical Stick","Bare Bow","Recurve Bow","Compound Bow"]
    

    def __init__ (self,name,weapon,type):
        global types
        global avaiweapons
        self.name = name
        self.weapon = weapon
        self.type = type

    def main(self):
        character = self.get_character()
        print(f"You are {character.name} a {character.type} with a {character.weapon}")

    def get_character(self):
        name = input("Enter your characters name: ")
        typeyn = False
        while typeyn == False:
            type = input(f"Enter you character type from the list {self.types}: ")
            type = type.lower().strip()
            if type == "knight":
                weapon = self.avaiweapons[0]
                self.urweapons.append(weapon)
                break
            if type == "wizard":
                weapon = self.avaiweapons[7]
                self.urweapons.append(weapon)
                break
            if type == "archer":
                weapon = self.avaiweapons[8]
                self.urweapons.append(weapon)
                break
            else:
                print("That is not a valid class, please try again.")
        
        character = Character(name,weapon,type)
        return character
    
if __name__ == "__main__":
    character = Character("", "","")
    character.main()

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

def tutorial():
    print(cowsay.fox(f"I am going to teach you how to play \n I have 50 health and you must roll a higher number than I do to be able to hit me. "))
    ur_dice_roll()
    game_dice_roll
        

#Weapon = sword & shield, bow, sword, 2 handed sword, 2 swords, spear, wand,staff, magical stick
#type = knight wizard/witch king/queen cavalry archer