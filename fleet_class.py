from robot_class import Robot


#This fleet class will instatiate 3 robots and put them in a list
 


class Fleet:
    def __init__(self):
        self.robots = []

    
    def create_fleet(self):
        robot_1 = Robot("Rob")
        robot_2 = Robot("Alexa")
        robot_3 = Robot("Siri")

        self.robots.append(robot_1)
        self.robots.append(robot_2)
        self.robots.append(robot_3)

