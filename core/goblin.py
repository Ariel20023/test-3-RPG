import random
class Goblin:
    def __init__(self,name):
        self.name = name
        self.hp = 20
        self.type =  " goblin "
        self.speed = random.randint(5, 10)
        self.power = random.randint(5,10)
        self.armor_rating = 1
        type_weapon = ["knife", "sword", "axe"]
        self.weapon = random.choice(type_weapon)


    def speak(self):
        print(self.type +" "+ self.name)



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