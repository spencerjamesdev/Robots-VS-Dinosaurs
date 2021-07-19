from fleet_class import Fleet
from herd_class import Herd


#this class is going to import from the dino class and robot class

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.battle()
        self.display_winners()

    def display_welcome(self):
        print("Welcome to the Battle!")

    def battle(self):
        while len(self.herd.dinos) > 0 and len(self.fleet.robots) > 0:
            self.robo_turn()
            self.dino_turn()


    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        self.show_robo_opponent_options()
        robot_choice = int(input("which robot will attack?"))
        self.show_dino_opponent_options()
        dino_choice = int(input("Which dinosaur will defend?"))
        self.fleet.robots(robot_choice).robot_attack(
            self.herd.dinos[dino_choice])
        if self.herd.dinos[dino_choice].health <= 0:
            self.herd.dinos.remove(self.herd.dinosaurs[dino_choice])


    def show_dino_opponent_options(self):
        print("Choose your dinosaur!")
        index = 0
        for dinosaur in self.herd.dinos:
            print(f"press {index} for {dinosaur.dino_name} with {dinosaur.dino_health}!")
            index += 1

    def show_robo_opponent_options(self):
        print("Choose your robot!")
        index = 0
        for robot in self.fleet.robots:
            print(f"press {index} for {robot.robot_name} with {robot.robot_health}!")
            index += 1
    def display_winners(self):
        if len(self.fleet.robots) > len(self.herd.dinos):
            print("The winners are Robots!")
        else:
            print("The winners are Dinosaurs!")