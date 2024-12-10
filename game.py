class Character:
    types = ["knight","wizard","archer"]
    avaiweapons = ["Sword","Shield","2 Handed Sword","2 Swords","Spear","Wand","Staff","Magical Stick"]
    urweapons = []
    inventory = []
    equipped = []

    def __init__ (self,name,weapon,type,item):
        global types
        self.name = name
        self.weapon = weapon
        self.type = type
        self.item = item

    def main():
        character = get_character()
        print(f"You are {character[0]} a {character[2]} with a {character[1]}")

    def get_character(self):
        name = input("Enter your characters name: ")
        type = input(f"Enter you character type from the list {types}")
        type = type.lower().strip()
        while type not in types:
            if type == "knight":
                weapon = "Sword"
            if type == "wizard":
                weapon = "Magical Stick"
            if type == "archer":
                weapon = "Bow"
            else:
                raise ValueError ("That is not a valid type")
        
        character = Character(name,weapon,type)
        return character




#Weapon = sword & shield, bow, sword, 2 handed sword, 2 swords, spear, wand,staff, magical stick
#type = knight wizard/witch king/queen cavalry archer