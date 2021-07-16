from robot_class import Robot


#This fleet class will instatiate 3 robots and put them in a list
robot_1 = Robot("Rob")
robot_2 = Robot("Alexa")
robot_3 = Robot("Siri")

class Fleet:
    def __init__(self):
        self.robot_fleet = []

    
    def create_fleet(self):
        self.robot_fleet = [robot_1, robot_2, robot_3]