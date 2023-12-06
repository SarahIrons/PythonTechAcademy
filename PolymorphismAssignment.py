""" POLYMORPHISM ASSIGNMENT
Create two classes that inherit from another class.
Each child should have at least two of their own attributes.
The parent class should have at least one method (function).
Both child classes should utilize polymorphism on the parent class method.
Add comments throughout your Python explaining your code. """

class Amphibian:
    feat1='hatch_from_eggs'
    feat2='gills_to_lungs'
    feat3='young_live_in_water'
    feat4_skin='varies'
    feat5_eggs='varies'
    feat6_movement='varies'
    
    def printFeat(self):
        print(self.feat1, self.feat2,self.feat3,self.feat4_skin,self.feat5_eggs,self.feat6_movement)

class Frog(Amphibian):
    feat4_skin='slimy_skin'
    feat5_eggs='cluster_eggs'
    feat6_movement='jump'


class Toad(Amphibian):
    feat4_skin='dry_warty_skin'
    feat5_eggs='eggs_in_chains'
    feat6_movement='walk'


F=Frog()
F.printFeat()

T=Toad()
T.printFeat()


##Above we describe Amphibian parent class and then Frog and Toad as children of Amphibian. This illustrates that they share common traits but also differ in certain ways.


      
