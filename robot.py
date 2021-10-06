from weapons import Weapons


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapons()

    def attack(self, dinosaur):
        pass
