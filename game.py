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
        print(f"You are {character[0]} a {character[2]} with a {character[1]}")

    def get_character(self):
        name = input("Enter your characters name: ")
        type = input(f"Enter you character type from the list {self.types}: ")
        type = type.lower().strip()
        weapon = ""
        while type not in self.types:
            if type == "knight":
                weapon == avaiweapons[0]
            if type == "wizard":
                weapon == avaiweapons[7]
            if type == "archer":
                weapon == avaiweapons[8]
            else:
                raise ValueError ("That is not a valid type")
        
        character = Character(name,weapon,type)
        return character
    
if __name__ == "__main__":
    character = Character("", "","")
    character.main()


#Weapon = sword & shield, bow, sword, 2 handed sword, 2 swords, spear, wand,staff, magical stick
#type = knight wizard/witch king/queen cavalry archer