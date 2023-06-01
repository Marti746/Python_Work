# PiP
# this is how to install 3rd party packages using pip (python index) availble at pypi.org
# go to the shell and put in pip install (name of package)
# Ex: pip install requests (will install globally for every python program)
# can also upgrade to the latest verion using pip insall -U (package name)

# can specify a specific verion or uninstall
# Ex: pip uninstall requests
# pip show (package) will show you info about the package

# List Compressions 
# are a way to create list in a precise way
numbers = [1, 2, 3, 4, 5]

numbers_power_2 = [n**2 for n in numbers]
print(numbers_power_2)
# list compressions are sometimes more prefered then loops as they are more readable and are written on a single line
# you can also use map

# Polymorphism
# generalizes a function so it can work on different types
# you can do a lot with this topic
class Lizard:
    def eat(self):
        print("Eating lizard food")
    
class Cat:
    def eat(self):
        print("Eating cat food")
    
animal1 = Lizard()
animal2 = Cat()

animal1.eat()
animal2.eat()

# Operator Overloading
class Dog:
    # the Dog class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other): # this will compare two dog objects to see which one is greater than 
        return True if self.age > other.age else False

roger = Dog('Roger', 8)
benny = Dog('Benny', 2)
print(roger > benny)

# can also create methods for arithemtic operators
#__add__() respond to the + operator
#__sub__() respond to the - operator
#__mul__() respond to the * operator
#__truediv__() respond to the / operator
#__floordiv__() respond to the // operator
#__mod__() respond to the % operator
#__pow__() respond to the ** operator
#__rshift__() respond to the >> operator
#__lshift__() respond to the << operator
#__and__() respond to the & operator
#__or__() respond to the | operator
#__xor__() respond to the ^ operator

# File "<stdin>", line 1
#     & C:/Users/HP/AppData/Local/Microsoft/WindowsApps/python3.10.exe c:/Users/HP/Desktop/Personal/PersonalCode/Python_Work/PythonLearning/Basics/polyandoveloadPython.py
#     ^
# SyntaxError: invalid syntax ( happens since I didnt exit() the termial properly when changing file name)