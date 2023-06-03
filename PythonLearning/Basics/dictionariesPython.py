# Dictionaries are another Essential Python Data Type
# Below we will work on and dive into some of the basics of Dictionaries and the features that can be used
# Dictionaries use the {} to make a dictionary opposed to [], ()
# Dictionaries use a key:value so below there will be a {key: value}
# the key can be any immutable value such as a string, number, or tuple 
# the value can be anything you want
dog = {"name": "Benny", "age": 2, "color": "Light Brown"} # name is key, Roger is value

# can access any of the values by using the notation below
# can use "" or '' to access the data
print(dog["name"])

# can also change the value using a similar notation
dog["age"] = 3

# Dictionaries have a nice method called get(key)
# this method allows the user to get information from the dictionary
print(dog.get("name"))
# the nice thing is it creates a default value
# the second part adds a default color if there isnt a color and that is brown
print(dog.get("color", "yellow"))
# get allows you to have  default value opposed to the bracket method which doesnt allow a default value

# dictionaries also have a pop() method just like that of the list
# dog.pop("name") will get us Benny and also removes it from the dictionary

# can also use popitem()
# it will retrieve and remove the last key:item pair in the dictionary
#print(dog.popitem())

# can use the in operator to see if a key is contained in a dictionary
print("color" in dog)
print(dog.keys()) # will print a list of all the keys within a dictionary called dict_keys
print(list(dog.keys())) # passing it into a list will return an actual list of all the key names

# can also do this with values
print(dog.values())
print(list(dog.values()))

# using the item() method will retrieve all the items within the dictionary and return them all within a list
print(list(dog.items()))
print(len(dog))

# adding a new key : item pair to the dictionary
dog["favorite food"] = "Meat"
print(dog)

# can also delete a key : item pair
# del dog['color']
# using the del will delete the key : value pair from the dictionary

# Copying a dictionary is not to hard
# copying a dictionary to another dictionary is as easy as using the .copy() function
# dogCopy = dog.copy()


# card_dealt = deal(2)
# card = card_dealt[0]
# rank = card[1]

# # add if statement to check to see if the rank is A and assign the value
# if rank == "A":
#     value = 11
# elif rank == "J" or rank == "Q" or rank == "K":
#     value = 10
# else:
#     value = rank

# rank_dict = {"rank" : rank, "value": value}

# print(rank_dict["rank"], rank_dict["value"])