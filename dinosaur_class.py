#dinosaurs need an object for name, health and attack power

class Dinosaur:
    def __init__(self, dino_name):
        self.dino_name = " "
        self.dino_attack_power = 25
        self.dino_health = 100


    def dino_attack(self, robot):
        robot.robot_health = robot.robot_health - self.dino_attack_power
