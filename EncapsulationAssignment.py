#ENCAPSULATION ASSIGNMENT
"""
Create a class that uses encapsulation. Requirements include:


1) This class should make use of a private attribute or function.

2) This class should make use of a protected attribute or function.

3) Create an object that makes use of protected and private.

4) Add comments throughout your Python explaining your code.

Upload your code to GitHub."""

#Using website 'pynative.com' for resource.

class Employee:
    #constructor
    def __init__(self, name, salary, age, project):
    #data members; the double underscore before salary marks it as private data, the single underscore before age denotes protected data
        self.name = name 
        self.__salary = salary #private
        self._age = age #protected
        self.project = project
          # public instance methods
#creating object of a class
#age is 90, salary is 120k
emp= Employee('Frick the Clown',120000, 90,'Clown Stuff')
#direct access to a private member using "name mangling"
print('Name: ',emp.name,'is working on', emp.project)

class Super:
  var1Occupation = None
  _var2Age = None
  __var3Salary = None

  def __init__(self,var1Occupation,_var2Age,__var3Salary):
    self.var1Occupation = var1Occupation
    self._var2Age = _var2Age
    self.__var3Salary = __var3Salary
 
    
    print("Information about Frick the Clown:")

  def FrickPublic(self):
    print("Public information: Frick's occupation: ",self.var1Occupation)

  def _FrickProtectedInfo(self):
    print("Protected information: Frick's age is " , self._var2Age)
  
  def __FrickPrivateInfo(self):
    print("Private information: Frick's salary is " ,self.__var3Salary)
  
  def accessFrickPrivateInfo(self):     
    # accessing private member function
    self.__FrickPrivateInfo()
    
  
#derived class
class Sub(Super):
  def __init__(self,var1Occupation, _var2Age, __var3Salary):
    Super.__init__(self,var1Occupation, _var2Age,__var3Salary)


Frick=Sub(' Clown Stuff', 90,' 120,000 dollars!')
Frick.FrickPublic()
Frick._FrickProtectedInfo()
Frick.accessFrickPrivateInfo()








