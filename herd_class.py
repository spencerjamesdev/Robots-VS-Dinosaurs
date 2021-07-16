from dinosaur_class import Dinosaur


#this class is going to create a list of dinosaurs
#name: 'rex'  attack power: 20   health: 100
dino_1 = Dinosaur("Rex", 20)
dino_2 = Dinosaur("Bran", 15)
dino_3 = Dinosaur("Tara", 35)

class Herd:
    def __init__(self):
        self.dino_list = []
    

    def create_herd(self):
        self.dino_list = [dino_1, dino_2, dino_3]

