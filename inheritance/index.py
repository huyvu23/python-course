# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
  pass

y = Student("Mike", "Olsen")
y.printname()

#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

# class Plumber(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)

# Use the super() Function: Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
class Plumber(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)