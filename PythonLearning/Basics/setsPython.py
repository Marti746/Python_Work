# Sets are another essential Data Structure within Python
# Sets work like tuples but can be changed unlike a tuple

# Below we will create a set
# Sets dont have key : item pairs like a dictionary
# Sets aren't ordered so thinking of them like mathematical is the way to go
# name = {"Roger", "Syd"}

set1 = {"Roger", "Syd", "Jack"}
set2 = {"Roger", "Nick"}

# intersecting two sets
# it will give you all the items that are in common between the two sets
intersect = set1 & set2
print(intersect)

# you can also create a union of two sets
# when making a union it is just a straight line "|"
# this will give you everything within both sets as one set
mod = set1 | set2
print(mod)

# can also get the difference between two sets
diff = set1 - set2
print(diff)

# can see if a set is a super set of another or a subset of another
super = set1 > set2
sub = set1 < set2

# len function can still count the amount of items within a set
# can also get a list of items by passing the set to the list() function
# can also use the in operator just like the others

# a set cannot have two of the same item
# if you have more then one item it will not add the second item to the set as it is already within the set