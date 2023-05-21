# List are a essenstial Python Data Structure 
# Below we will work on and dive into some of the basics of lists
# Allows you to group values together under a common name
dogs = ["Shiba", "Borderdoodle", "Golden Retriever", "German Sheperd", "Pitbull", "Wiener Dog"]

# can mix multiple data types within a list
new_dogs = ["Benny", 1, True, "Teddy", 12, False]
# in operator to check if it is within the list
print("Benny" in new_dogs)
print("Rimuru" in new_dogs)

# can also refrence based on index
# can use negative numbers and it will start at the back of the list
print(new_dogs[0]) # benny
print(new_dogs[3]) # teddy
print(new_dogs[-2]) # 12

# can also change the values within the list through the index
dogs[0] = "Black Lab"
print(dogs)

# looping through an array from a certain point to another point [inclusive: exclusive]
# leaving the first blank will start at the beginning
# leaving the last blank will go until the end of the list
print(dogs[1:3])

# len function tells you the length of a list
print(len(dogs))
print(len(new_dogs))

# append() method allows us to add another item to the list
dogs.append("Shibu Inu")

# can also use extend()
# can pass in another list with the extend method
dogs.extend(["Terriar", "Bloodhound"])
print(dogs)

# can also use the += operator
# both the += and extend take the list and add it to the end of the current list
# forgetting the square brackets will add each letter indavidually to the current list
# dogs += ["Terriar", "Bloodhound"]

# lists also have removal of objects
# using the remove() method allows us to remove an item from the list
dogs.remove("Pitbull")
print(dogs)

# pop() function removes the last element in the list
print(dogs.pop())
print(dogs)

# insert() method allows you to put a item in a certain index of the list
# insert(index, item)
dogs.insert(4, "pitbull")
print(dogs)

# can also add multiple items at certain point in the list
# to do this we need to do it with a slice
# ex: dogs[1:1] = ["Test1", "Test2"]

print("========== Sorting Content ==================")
# Sorting of a list
# python has a built in sort() method 
# sorting does modif the list content so to avoid that you can copy the list content using newlist = list[:]
# using the slice makes sure that you get all the elements from the old list into the new list
# however using new_dogs.sort() gives an error as there are multiple variable types within the list
# using sort() on the dogs list will work
dogs.sort()
print(dogs)

# sort method sorts upper case first then lower case when sorting a list of strings
# can make it so it sorts based on the letter
dogs.sort(key=str.lower)
print(dogs)

# there is a way to sort a list without modifing the current list
# the method sorted(iterable, key, reverse) 
# sorted() method doesnt modify the current list so printing the list will give you a differnt list than the sorted list
sorted(dogs, key=str.lower)