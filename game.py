from core.player import *
from core.goblin import *
from core.orc import *
class Game:


    def show_menu(self):
        choice = input("Fight or escape")
        return choice



    def create_player(self):
        name = input("choice a name")
        player = Player(name)
        return player




    def choose_random_monster(self):
        name = input("choice a monster name")
        type_of_monster = ["orc","goblin"]
        choice = random.choice(type_of_monster)
        if choice == "orc":
            monster = Orc(name)
            return monster
        monster = Goblin(name)
        return monster




    def roll_dice(self,sides) :
        if sides == 6:
            choice = random.randint(0,6)
        else:
            choice = random.randint(0,20)
        return choice




    def who_first(self,player, monster):
        a_player_cube = self.roll_dice(6) + player.speed
        monster_cube = self.roll_dice(6) + monster.speed
        if a_player_cube >= monster_cube:
            start = player
        else:
            start = monster
        return start





    def battle(self,player, monster):
        start = self.who_first(player, monster)
        if start == player:
            other = monster
        else:
            other = player
        while start.hp > 0 and other.hp > 0:
            damage = start.attack(start, other)
            if damage <= 0:
                print(f"{other.name}Dead, game over")
            else:
                start,other = other,start




    def start(self):
        choice = self.show_menu()
        if choice == "Fight":
            player = self.create_player()
            player.speak()
            monster = self.choose_random_monster()
            monster.speak()
            self.battle(player,monster)
        else:
            print("goodbye")



