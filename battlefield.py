from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.fleet.create_fleet()
        self.herd.create_herd()

    def run_game(self):
        print('Welcome to Robots vs Dinosaurs! In this game you will choose your team and battle until you finish the enemy. ')
        self.display_welcome()
        # welcome message
        # display rules

        # dinosaurs go first
        # one dinosaur attacks one robot
        # robots go next
        # display winner

    def display_welcome(self):
        team_choice = input(
            "Time to pick your team. Type 'robo' for Robots or 'dino' for Dinosaurs. ")
        if team_choice == 'robo':
            print('You have chosen the fleet of Robots as your team!')
        elif team_choice == 'dino':
            print('You have chosen the herd of Dinosaurs as your team!')
        else:
            self.display_welcome()

        self.dino_turn()

    def battle(self):
        while len(self.herd.dinosaurs) > 0 and len(self.fleet.robots) > 0:
            self.dino_turn()
            self.robo_turn()

            # continue looping through fighting turns

            # end the loop

        # while loop what is below until dino or robo are all at health=0
        # robot_one vs dinosaur_one
        # robot_two vs dinosaur_two
        # robot_three vs dinosaur_three

    def dino_turn(self):
        dino_attack_one = self.herd.dinosaurs[0]
        dino_attack_one.attack(self.fleet.robots[0])
        if self.fleet.robots[0].health == 0:
            self.fleet.robots.pop(0)

        if self.herd.dinosaurs[1] and self.fleet.robots[1]:
            dino_attack_two = self.herd.dinosaurs[1]
            dino_attack_two.attack(self.fleet.robots[1])
            if self.fleet.robots[1].health == 0:
                self.fleet.robots.pop(1)

        if self.herd.dinosaurs[2] and self.fleet.robots[2]:
            dino_attack_three = self.herd.dinosaurs[2]
            dino_attack_three.attack(self.fleet.robots[2])
            if self.fleet.robots[2].health == 0:
                self.fleet.robots.pop(2)

        if len(self.fleet.robots) == 0:
            print('Game is over')
        else:
            self.robo_turn()
         # game over
        # # robot_defense_one = Fleet[0]
        # dino_attack_one.dinosaurs.attack
        # dino(one,two and three) attacks robo(one,two and three) and robo(s) lose health depending on dino attack power (call the attack method in dino file)

    def robo_turn(self):
        robo_attack_one = self.fleet.robots[0]
        robo_attack_one.attack(self.herd.dinosaurs[0])
        if self.herd.dinosaurs[0].health == 0:
            self.herd.dinosaurs.pop(0)

        if self.fleet.robots[1] and self.herd.dinosaurs[1]:
            robo_attack_two = self.fleet.robots[1]
            robo_attack_two.attack(self.herd.dinosaurs[1])
            if self.herd.dinosaurs[1].health == 0:
                self.herd.dinosaurs.pop(1)

        if self.fleet.robots[2] and self.herd.dinosaurs[2]:
            robo_attack_three = self.fleet.robots[2]
            robo_attack_three.attack(self.herd.dinosaurs[2])
            if self.herd.dinosaurs[2].health == 0:
                self.herd.dinosaurs.pop(2)

        if len(self.fleet.robots) == 0:
            print('Game is over')
        else:
            self.battle()
        # robo(one,two and three) attacks dino(one,two and three) and dino(s) lose health depending on robo weapon attack power (call the attack method in robo file) End the round.

    def show_dino_opponent_options(self):
        # display remaining health
        pass

    def show_robo_opponent_options(self):
        # display remaining health. Run fights again until fleet or herd = zero health
        pass

    def display_winners(self):
        # Once herd or fleet reach zero health, display other as winners
        pass
