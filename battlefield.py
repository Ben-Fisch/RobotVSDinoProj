from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        print('Welcome to Robots vs Dinosaurs! In this game you will choose your team and battle until you finish the enemy. ')

    def display_welcome(self):
        team_choice = input(
            "Time to pick your team. Type 'robo' for Robots or 'dino' for Dinosaurs. ")
        if team_choice == 'robo':
            print('You have chosen the fleet of Robots as your team!')
        elif team_choice == 'dino':
            print('You have chosen the herd of Dinosaurs as your team!')
        else:
            input(
                "Time to pick your team. Type 'robo' for Robots or 'dino' for Dinosaurs. ")

    def battle(self):
        pass

    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass
