programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    
}

# Create and empty dictionary
empty_dictionary = {}

# Retrieving items from dictionary
print(programming_dictionary["Bug"])

# Adding new items to dictionary
programming_dictionary["Loop"] = "the action of doing something over and over again"
print(programming_dictionary)

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(f"{key}")
    print(programming_dictionary[key])
