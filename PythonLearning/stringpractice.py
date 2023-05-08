# Work with strings and string methods
# 'Hello World!' == "Hello World!" == """Hello World!"""
# "hello".capitalize() == "Hello"
# "hello".replace("o", "i") == "helli"
# "hello".isalpha() == True
# "985".isdigit() == True #useful when converting to int
my_str = 'Hello World!'

print(my_str)          # Prints complete string
print(my_str[0])       # Prints first character of the string
print(my_str[2:5])     # Prints characters starting from 3rd to 5th
print(my_str[2:])      # Prints string starting from 3rd character
print(my_str * 2)      # Prints string two times
print(my_str + "TEST\n") # Prints concatenated string

# Creates a list of variables
# list can have multiple different types of variables
list = ["abcd", 987, 6.69, "John", 70.2]
tinylist = [123, 'john']

print(list)              # Prints complete list
print(list[0])           # Prints first element of the list
print(list[1:3])         # Prints elements starting from 2nd till 3rd 
print(list[2:])          # Prints elements starting from 3rd element
print(tinylist * 2)      # Prints list two times
print(list + tinylist)   # Prints concatenated lists

