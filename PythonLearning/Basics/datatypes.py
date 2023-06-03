# Work on and indepth on the boolean values in python
# Needs to have a capital T or F or else it isnt a true boolean value
# If you put 0 it evalutates to false if you put anything else it is true
done = True
# done = False

print(type(done) == bool)

if done:
    print("yes")
else:
    print("No")

# any() function returns true if any of the values of the iterable are true
book1_read = True
book2_read = False
readAny = any([book1_read, book2_read])

# all() function is similar but returns true if all the values are true
ingredients_purchased = True
meal_cooked = False
readyToServe = all([ingredients_purchased, meal_cooked]) # would be False

# Number Data types other than int and float
# Complex data type imaginary numbers are written with a j suffix
num1 = 2+3j
num2 = complex(2,3) # 3 would be the imaginary number

print(num1.real, num1.imag)

# Built in Functions for numbers and helping
# abs() is the absolute value
print(abs(-5.5))
# round() will round to the nearest integer
# will round up if >= .5
print(round(5.5)) # 6
print(round(5.49)) # 5
# adding a second parameter will specify how many decimals it will be precised on
# 1 would round to the nearest decimal point on tenths place
print(round(5.49, 1))

# Enums
# enums are a readable name that are bounded to a constant value
# would need to import enum from the enum library
from enum import Enum

# State can be any word we want it is a variable that will have inactive and active
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE) # will just print out State.ACTIVE
print(State.ACTIVE.value) # will print the value of the active variable
print(State(1)) # Will return State.Active since you can send it the value
print(State['ACTIVE']) # can use the [] to also access the state

# Only way to make a constant in Python
# can also list all the values
print(list(State))
# can also count them
print(len(State))

# User input within Python
age = input("What is your age: ")
print("Your age is " + age)
# can also use the print("f/") to put in a quick add to the string without the concatenation

# Control statements
condition = True
name = "Roger"

if condition == True:
    print("The Condition ")
    print("was true")
else:
    print("The Condition ")
    print("was true")
print("Outside the if and else")

# can also have multiple using the if, elif, and else
# if condition == True:
#     print("Was true")
# elif name == "Roger":
#     print("Hello Roger")
# elif name == "Syd":
#     print("Hello Syd")
# elif name == "Lorenzo":
#     print("Hello Lorenzo")
# else:
#     print("It was false")