#https://www.w3schools.com/python/python_classes.asp

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
p1.myfunc()

# Modify Object Properties
p1.age = 40
print(p1.age)
# Delete Object Properties
# del p1.age
print(p1.age)  # This will raise an AttributeError since age has been deleted

# pass statement
class trump:    
    pass