# Classes
# we can create our own types and instatiate our own objects
# inheritance is another important part of classes
class Animal:
    def walk(self):
        print("Walking...")

class Dog(Animal): # adding parathesis will have it inherit the animal class
    def __init__(self, name, age): # constructor for the dog class
        self.name = name # will assign name and age
        self.age = age

    def bark(self): # self will point to the current object instance
        print("woof!")

doggy = Dog("Benny", 2)
#print(type(roger))
print(doggy.name)
print(doggy.age)
doggy.bark()
doggy.walk()

# Modules
# if python script is under different folder you will need to create a __init__.py file which tells it that it has modules
# then you do from (folder) import (filename) or from (folder).(filename) import (methodname)

# every python file is a module
# can create a software with multiple python scripts
# can also use the from import syntax
# import dog
# dog.speak()
from dog import speak
speak()

# Python standard library has a lot of different utilites
# math for math utilities
# re for regular expressions
# json to work with JSON
# datetime to work with dates
# sqlite3 to use SQLite
# os for Operating System utilities
# random for random num generator
# statistics for statistics utilities
# requests to perform HTTP network requests
# http to create HTTP servers
# urllib to manage URLs

# Accepting Arguments
# this includes the command line for python
# to usually run the file you use python filename.py
# the .\filename.py will open a file for you
#import sys
#print(sys.argv)  # doing this will print a list of the command line arguments
#python filename.py beau 39  -> ['filename.py', 'beau', '39']
# argv is a list of items so you can do name = sys.argv[1]

# another library that python has is import argparse
# then you can do this
# parser = argparse.ArgumentParser[description='This program prints the name of my dog']
# this will be the description of the program and then you add arguments you wan to accept
# such as... and you can have before required have choices={red, yellow}
# parser.add_argument('-c', '--color', metavar='color', required=True, help='the color to search for')
# args = parser.parse_args()
# then you can print it if you wanted with print(args.color)
# to call it you use python main.py -c red