from fleet_class import Fleet
from herd_class import Herd


#this class is going to import from the dino class and robot class

class Battlefield:
    def __init__(self):
        self.robot_fleet = Fleet.create_fleet()
        self.dino_herd = Herd.create_herd()

    def run_game(self):
        return True

    def display_welcome(self):
        print("Welcome to the Battle!")

    def battle(self):
        return True

    def dino_turn(self, dinosaur):
        self.dinosaur.dino_attack()

    def robo_turn(self, robot):
        self.robot.robot_attack()

    def show_dino_opponent_options(self):
        for i in self.robot_fleet():
            print(str(i) + "is at" + str(i.robot_health) + "Health")

    def show_robo_opponent_options(self):
        for i in self.dino_herd():
            print(str(i) + "is at" + str(i.dino_health) + "Health")

    def display_winners(self):
        print("The winners are ")