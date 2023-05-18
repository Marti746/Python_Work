# List are a essenstial Python Data Structure 
# Below we will work on and dive into some of the basics of lists
# Allows you to group values together under a common name
dogs = ["Shiba", "Borderdoodle", "Golden Retriever", "German Sheperd"]

# can mix multiple data types within a list
new_dogs = ["Benny", 1, True, "Teddy", 12, False]
# in operator to check if it is within the list
print("Benny" in new_dogs)
print("Rimuru" in new_dogs)

# can also refrence based on index
print(new_dogs[0]) # benny
print(new_dogs[3]) # teddy

# can also change the values within the list through the index
dogs[0] = "Black Lab"
print(dogs)