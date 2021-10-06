from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        robot_one = Robot('Bob')
        robot_two = Robot('Tina')
        robot_three = Robot('Billy')
        self.robots.append(robot_one)
        self.robots.append(robot_two)
        self.robots.append(robot_three)
