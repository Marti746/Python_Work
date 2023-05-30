# Functions 
# Allows us to create a set of instructions for the computer to follow
# The indent can be either 2-4 spaces as long as it is the same amount
# Allows us to break down code into different parts and helps with readability
# functions can accept 1 or more parameters and should be descriptive
def hello(name="my friend"):
    print("Hello! " + name)
# this is a function with the body of the function being after the colon
# to call a function you call it like other langauges (can call it as many times as you want)
hello("Benny")

# parameter vs arguments
# parameters are the values accepeted by the function inside the function definition
# arguments are the values we pass to the function when we call it
# arguments can have a default value if not specified
hello()
# adding a = to the argument will give it the default value of my friend when you call it above
def multiValue(name, age):
    print("Hello, " + name + " you are " + str(age) + " years old")
    return age

multiValue("Benny", 2)
# parameter are passed by reference
# below is an example
def change(value):
    value["age"] = 2

# val = 1 (immutable)
val = {"age" : 1}
change(val)
print(val)
# a object that would be mutable would be like a dictionary
# a function can also return a value with the return statement (see above for the example)
# like java, c#, c++ you can also just put a return with no value
# functions are very similar to that of other languages
# example of function with if-return
# can also return comma seperate value return name, "Benny", 8
def hello2(name):
    if not name:
        return
    print("Hello " + name + "!")

hello2(False)
hello2("Benny")

# variable scope
# if you create a variable outside or above a funciton that is called a global variable
# if declared inside a function it is a local variable and only visible inside the function
age = 8 # Global variable

def test():
    # age = 8 # local variable
    print(age)

print(age)
test()

# Nested Functions
# Functions in python can be nested within other functions
# functions are only visible within that function if nested
# its good to hide functionality within a function if it isnt useful elsewhere in your program
# we can also make use of closures
def talk(phrase):
    def say(word):
        print(word)
    
    words = phrase.split(" ")
    for word in words:
        say(word)

talk("I am going to buy the milk")

# another example of nested functions within python
def count():
    count = 0

    def increment():
        nonlocal count  # nonlocal allows us to access the variable count above the increment() function
        count = count + 1
        print(count)
    
    increment()

count()

# Clousres
# If you return a variable from a nested function to another function it has access to the variable in that funciton even if not active
def counter():
    count = 0

    def increment():
        nonlocal count  # nonlocal allows us to access the variable count above the increment() function
        count = count + 1
        return count
    
    return increment

increment = counter()
print(increment()) # 1 we are calling the inner function so it doesnt reset the count variable 
print(increment()) # 2
print(increment()) # 3