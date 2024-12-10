import re
import cowsay

class Character:
    types = ["knight","wizard","archer"]
    avaiweapons = ["Sword","Shield","2 Handed Sword","2 Swords","Spear","Wand","Staff","Magical Stick","Bare Bow","Recurve Bow","Compound Bow"]
    urweapons = []
    inventory = []
    equipped = []

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
        type = input(f"Enter you character class from the list {self.types}: ")
        type = type.lower().strip()
        while type not in self.types:
            type = input(f"Enter you character type from the list {self.types}: ")
            type = type.lower().strip()
            if type == "knight":
                weapon = self.avaiweapons[0]
            if type == "wizard":
                weapon = self.avaiweapons[7]
            if type == "archer":
                weapon = self.avaiweapons[8]
            else:
                print("That is not a valid class, please try again.")
        
        character = Character(name,weapon,type)
        return character
    
if __name__ == "__main__":
    character = Character("", "","")
    character.main()



#Weapon = sword & shield, bow, sword, 2 handed sword, 2 swords, spear, wand,staff, magical stick
#type = knight wizard/witch king/queen cavalry archer