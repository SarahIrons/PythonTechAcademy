#CLASS CHALLENGE
#Complete these actions:
#Create a class.
class Pants:
    def __init__(self,color,cut,fit):
        self.color= color
        self.cut = cut
        self.fit = fit
    def PantsInventory(self):
        print('Do you like to wear ' + self.fit+ ' pants?')
p1=Pants('gray','wideleg','loose-fit')
p1.PantsInventory()
#Create an object:
    #object is pants
#Assign values to object properties using the __init__() function.
    #values are color, cut, and fit type.
#Create a method in a class.
    #method is 'pants inventory' to return a question string of 'do you like to wear loose-fit pants'?
