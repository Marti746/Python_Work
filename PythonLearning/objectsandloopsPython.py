# Objects
# everything in python is a object even values of basic types are objects
# objectys have attributes and method using the dot syntax
age = 8
print(age.real)
print(age.imag)
print(age.bit_length())

# a list has different methods
items = [1, 2, 3]
items.append(4)
items.pop()

# methods depend on the type of value you have each have different methods that can be called
# id allows you to see where it is in memory the location in the memory
print(id(items))
# most objects in python are immutable objects 
# age = age + 1 creates a new value to reassign it

# Loops
# essential to programming in python we have 2 loops While Loops and For Loops
condition = True
while condition == True:
    print("The condition is True!")
    condition = False
# while loops repeat their block until the condition is false
# above is a infinite loop and will go on forever common to add a counter
# example of a counter to stop the while loop
count = 0
while count < 8:
    print("The condition is True")
    count = count + 1 # can also do count += 1

print("After the loop")

# other type of loop is the for loop
# using the for loop we can tell python to execute a block of code without a condition
# can also get the index of the list you use the enumerator function
# example using a list
itemList = [1, 2, 3, 4] 
names = ["benny", "jack", "nick", "david"]
#for item in itemList:
for index, item in enumerate(names): # will get the index and item
    print(index, item)

# you can also use the range function to iterate through a certain amount of values
for item in range(10):
    print(item)

# both While and For loops can be interupted using the break and continue method
numList = [1, 2, 3, 4]
for item in numList:
    if item == 2:
        continue # this will skip the iteration
        #break # this will break the loop and stop iterating
    print(item)