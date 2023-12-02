# variable practice in python
# Variables can only us numbers, letters, underscores
# Cannot start with a number
# Cannot use a space
# Best to avoid Python Keywords

# Python has 5 standard data types Numbers,String,List,Tuple,Dictionary
# Supports 4 different numerical types int,long,float,complex

my_age = 22
my_name = "Zynda"
my_major = "Computer Science"
my_money = 420.69

# The (\) allows the string to conitnue on the next line if it is too long
print(f"My name is {my_name}. I am {my_age} and I am currently studying \
{my_major}. I am trying to get a job since I only have {my_money}.")


# variables can all be assigned on same line too
a,b,c = 1,2,"Benny"
print(a, b, c)

# Using the del function can delete a variable
# completly deletes the variable so it doesn't exist anymore
var1 = 1
print(var1)
del var1

# Arithmetics with variables
# Doesn't complain about two types being added together
# It will produce desired results no matter
results = 42
pi = 3.14159
print(results + pi)
total = (results * pi) / 2
print(total)

# Casting variables
int(pi) == 3
float(results) == 46.2
print(pi)
