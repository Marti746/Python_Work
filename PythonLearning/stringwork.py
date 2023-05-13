# This is string work and multi line strings
# This is multi line strings
print("""David is

22

years old
""") # Will print just like this can also use single quotes as long as its 3

# String methods
print("david".upper()) # also has a .lower()
print("david".title()) # makes the first letter of each word capital
print("DaVid".islower()) # tests to see if all are lower same with upper .isupper()

# all of these below methods return a new modified string and doesnt change the original string

# startswitch() to check if the string starts with a specific string
# endswitch() to check if the string ends with a specific substring
# replace() to replace a part of a string
# split() to split a string on a specific character separator
# strip() to trim the whitespace from a string
# join() to append new letters to a string
# find() to find the position of a substring

# isalpha() to check if a string contains only characters and is not empty
# isalnum() to check if a string contains characters or digits and is not empty
# isdecimal() to check if a string contains digit and is not empty

# len(str) gives the length of the string

# This is a example to show
name = "David"
print(name.lower())
print(len(name))
print("vi" in name) # sees if vi is within the name

newName = "Dav\"id" # with adding the back slash to the string it tells python to just ignore the middle quote
# can also do a single quote at the beginning and end then a double quote you dont need the backslash
# newName = 'Da"\'vid'
# \n within the string adds a new line
# when adding a backslash to a string you need to add 2 of them 
# EX: "Be\\au"

print(name[1]) # Gets the letter at index 1 of the string
print(name[-1]) # Starts counting at the of the string 
print(name[1:3]) # slicing where every character starting at 1 and ending at 3/ Putting a blank makes it start at the beginning