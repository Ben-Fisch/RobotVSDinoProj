from weapons import Weapons


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapons()

    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.weapon.attack_power

        # for each robot attack, decrease dinosaur helth by Weapons attack_power (-10)
