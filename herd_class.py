from dinosaur_class import Dinosaur


#this class is going to create a list of dinosaurs
#name: 'rex'  attack power: 20   health: 100


class Herd:
    def __init__(self):
        self.dinos = []
    

    def create_herd(self):
        dino_1 = Dinosaur("Rex")
        dino_2 = Dinosaur("Bran")
        dino_3 = Dinosaur("Tara")
        
        
        self.dinos.append(dino_1)
        self.dinos.append(dino_2)
        self.dinos.append(dino_3)
        

