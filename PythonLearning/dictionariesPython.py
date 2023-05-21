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