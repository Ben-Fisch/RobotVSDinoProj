from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        dinosaur_one = Dinosaur('Frank', 5)
        dinosaur_two = Dinosaur('Lori', 10)
        dinosaur_three = Dinosaur('Dante', 20)
        self.dinosaurs.append(dinosaur_one)
        self.dinosaurs.append(dinosaur_two)
        self.dinosaurs.append(dinosaur_three)
    # should be pushed to the list of dinos above
