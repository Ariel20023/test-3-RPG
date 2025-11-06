import random
class Orc:
    def __init__(self,name):
        self.name = name
        self.hp = 50
        self.type  =  " orc "
        self.speed  =random.randint(0,5)
        self.power = random.randint(10,15)
        self.armor_rating  = random.randint(2,8)
        type_weapon = ["Knife","Sword","Axe"]
        self.weapon  =random.choice( type_weapon)

    def speak(self):
        print(self.type +" "+self.name)



    def roll_dice(self, sides):
        if sides == 6:
            choice = random.randint(0, 6)
        else:
            choice = random.randint(0, 20)
        return choice



    def attack(self, start, other):
        Rolling_a_twenty_digit_die = self.roll_dice(20)
        p = start.speed + Rolling_a_twenty_digit_die
        if p > other.armor_rating:
            rolling_a_cube = self.roll_dice(6)
            damage = start.power + rolling_a_cube
            other.hp -= damage
        return other.hp

