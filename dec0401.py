#parent class
class Organism:
    name = "unknown"
    species = "unknown"
    legs = None
    arms = None
    DNA = "Sequence A"
    origin = "unknown"
    carbon_based = True

    def information(self) :
        msg = "\n Name: {},\nSpecies:\n{}Legs:{}\nArms:{}\nDNA:{}\nOrigin:{}\nCarbon based:{}".format(self.name, self.species,self.legs,self.arms,self.DNA,self.origin,self.carbon_based)
        return msg
    

#child class instance
class Human(Organism):
    name = 'MacGuyver'
    species= 'Homosapien'
    legs= 2
    arms= 2
    origin= 'Earth'

    def ingenuity(self):
        msg = "\nCreates  deadly weapon using only a paperclip, gum and duct tape."
        return msg

#another child class instance
class Dog(Organism):
    name = "Spot"
    species= 'Canine'
    legs = 4
    arms= 0
    DNA = "Sequence B"
    Origin = 'Earth'

    def bite(self):
        msg = "\nEmits a low menacing growl and bites down ferociously on its target."
        return msg

#another child class instance
class Bacterium(Organism):
    name = "X"
    species= "Bacteria"
    legs = 0
    arms= 0
    DNA = "Sequence C"
    Origin = 'Mars'

    def replication(self):
        msg = "\nThe cells begin to divide and multiply into two separate organisms."
        return msg
    
if __name__ == "__main__":
    human= Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacteria= Bacterium()
    print(bacteria.information())
    print(bacteria.replication())
    
