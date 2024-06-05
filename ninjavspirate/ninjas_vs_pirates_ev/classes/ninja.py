import random

class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        self.spell = 7
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , target ):
        print(f"{self.name} is attacking {target.name}.")
        dmgRoll = random.randint(1, 20)
        target.defend(self.strength + dmgRoll)
        return self
    
    def heal (self):
        healRoll = random.randint(1,4)
        healPoints = self.spell * healRoll
        self.health += healPoints
        print(f"{self.name} heals themself for {healPoints} points. They now have {self.health} health. \n")
        return self
    
    def defend(self, damage):
        damage -= self.speed
        self.health -= damage
        print(f"{self.name}: Ouch!")
        print(f"{self.name} takes {damage} damage, they now have {self.health} health.\n")
        return self