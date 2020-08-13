import random

# RPG Character has:
# race
# class
# ability tree

class rpgCharacter:
    def __init__(self, name, race, charclass, abilities, level, health, xp):
        self.name = name
        self.race = race
        self.charclass = charclass
        self.abilities = abilities
        self.level = level
        self.health = health
        self.xp = xp
   
    def addXp(self, newxp):
        self.xp = (self.xp + newxp) 

    def levelUp(self):
        self.level = (self.level + 1)

    def heal(self, health):
        self.health = (self.health + health)

    def damage(self, damage):
        self.health = (self.health - damage)

    def attack(self):
        ability_check = random.randrange(20) 
        damage   = random.randrange(6)

        retval = 0
        if(ability_check >= 10):
            retval = damage
     
        return retval

    def status(self):
        print("\n")
        print("Hero: " + self.name)
        print("Level: " + str(self.level) + " - " + self.race + " " + self.charclass)
        print("Health: " + str(self.health) + " XP: " + str(self.xp))
        print("Abilities: " + str(self.abilities)) 
        print("\n")

