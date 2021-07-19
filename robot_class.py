from weapon_class import Weapon


#Robot needs to have a name and health
class Robot:
    def __init__(self, robot_name):
        self.robot_name = " "
        self.robot_health = 100
        self.robot_weapon = Weapon("Ray-Gun", 20)


    def robot_attack(self, dinosaur):
        dinosaur.dino_health = dinosaur.dino_health- self.Weapon.weapon_attack_power
 

