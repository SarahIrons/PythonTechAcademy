#INHERITANCE CHALLENGE
#Create a child class that inherits functionality from a parent class.
#the member class is the parent class. Teacher and student are children of Member. 
class Member:
        def __init__(self, f_name, l_name, IDNo):
                self.f_name = f_name
                self.l_name = l_name
                self.IDNo = IDNo

        def printname(self) :
                print(self.f_name, self.l_name)
    
class Teacher(Member):
    Subject='English'
    Years_of_service = 5

class Student(Member):
    Passing= True
    Grade = 9

x = Teacher("Jane","Morris",4567)
x.printname()

