import random
class Player:
    def __init__(self,name):
        self.name = name
        self.speed  = random.randint(5,10)
        self.armor_rating = random.randint(5,15)
        self.power = random.randint(5,10)
        prof = ["fighter", "cure"]
        self.profession = random.choice(prof)
        if self.profession == "fighter":
            self.hp = 50
            self.power += 2
        else:
            self.hp = 60


    def speak(self):
        print(self.name)

    def roll_dice(self,sides) :
        if sides == 6:
            choice = random.randint(0,6)
        else:
            choice = random.randint(0,20)
        return choice


    def Damage_calculation_if_it_a_monster(self,damage,monster):
            if monster.weapon == "knife":
                damage = damage * 0.5
            elif monster.weapon == "sword":
                damage = damage
            else:
                damage = 1.5 * damage
            return damage

    def attack(self, start, other):
        Rolling_a_twenty_digit_die = self.roll_dice(20)
        p = start.speed + Rolling_a_twenty_digit_die
        if p > other.armor_rating:
            rolling_a_cube = self.roll_dice(6)
            damage = start.power + rolling_a_cube
            damage = self.Damage_calculation_if_it_a_monster(damage, other)
            other.hp -= damage
        return other.hp

























