#the member class is the parent class. Teacher and student are children of Member. 
class Member:
    f_name = 'First'
    l_name= 'Last'
    IDNo = 4321

class Teacher(Member):
    Subject='English'
    Years_of_service = 5

class Student(Member):
    Passing= True
    Grade = 9
    
