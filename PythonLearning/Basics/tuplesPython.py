# Tuples are another Python Data Type
# Below we will work on and dive into some of the basics of Tuples and the features that can be used
# Allow you to create immutable groups of objects, Once created it cant be modified
# Tupels use () opposed to []
names = ("David", "Parker", "Nick", "Jack")

# can also use the same index methods that a list can
# using a negative number will start searching from the end
names[2]
names.index("Parker")
# can also count the amount of items within a tuple with the len function
len(names)

# also allows you to use the in operator just like a list
# also allows extract with slices [:]
print("David" in names)
names[0:5]

# can also use the sorted() function
# just like a list it will create a new tuple and not modify the current tuple
# ex: sorted(names)
print(sorted(names, key=str.lower))
print(names)

# can also create a new tuple with the plus(+) operator
newTuple = names + ("Kevin", "Josh", "Jill", "Nathan", "Bianca")

# this is the only way to modify a tuple as you cant ever modify a tuple once created since it is a immutable type