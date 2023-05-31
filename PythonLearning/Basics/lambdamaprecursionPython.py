# Lambda Functions
# lambda functions are tiny function and have one expression in their body
lambda num : num * 2 # returns num * 2

multiply = lambda a, b : a * b
# lambda cant be invoke directly but can be assigned to variables
print(multiply(2, 4))

# Map(), Filter(), Reduce()
# maps are used to run a function on a iterable item such as a list and create new list
# Ex:
numbers = [1, 2, 3]

# regular way to do it but can be done with a lambda
# def double(a):
#     return a * 2

# can be simplified even more
# double = lambda a : a * 2
result = map(lambda a : a * 2, numbers)
# result = map(double, numbers)
print(list(result))

# Filter
# filter takes a iterable and return a filter object which return some of it without the original items sometimes
numbers1 = [1, 2, 3, 4, 5, 6]

# def isEven(n):
#     return n % 2 == 0

result1 = filter(lambda n : n % 2 == 0, numbers1) 
# result = filter(isEven, numbers1)
print(list(result1))

# Reduce()
# reduce is used to calculate a value out of a sequence
# reduce has to be imported from the functools library
from functools import reduce
expenses = [("Dinner", 80), ("Car Repair", 120)]

# long way to do it without reduce()
# sum = 0
# for expense in expenses:
#     sum += expense[1]
sum = reduce(lambda a, b: a[1] + b[1], expenses)

print(sum)

# Recursion
# factorial calculation is the best way to show recursion
# 3! = 3 * 2 * 1 = 6
def factorial(n):
    if n == 1: return 1  # needs to have a base case or else it will give you a recursion error
    return n * factorial(n-1)

print(factorial(3))
print(factorial(4))
print(factorial(5))

# Decorators
# decorators are a way to enhance, change, or alter how a function works
# decorators are defined with teh @ symbol with the function name
# Ex:
def logtime(func):
    def wrapper():
        print("before")
        # do something before
        val = func()
        print("after")
        # do something after
        return val
    return wrapper

# create a decorator
# takes a function as a parameter and wraps it in an inner function and then returns that inner function
@logtime
def hello():
    print("Hello")

hello()

# Docstrings
# another way to add a comment
# Ex:
def increment(n):
    """Increment a number"""
    return n + 1

# Placing a docstring at the top of the file is similar to multi line comments in other langauges
""" Example Docstring

This is a example of a header docstring that can be made
- Dog
... blah blah blah
"""
# can then use the help function to get the doctring
# print(help(class/function))

# Annotations
# Python is a dynamic type langauge 
# Annotations allow us to optionally do that
# Ex without annotations:
# def increment(n):
#     """Increment a number"""
#     return n + 1
# with the below we are specifying that we want to recieve a int and return a int
def incrementMe(n: int) -> int:
    return n + 1
# can do the same with variables
count: int = 0
