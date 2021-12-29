
# Python Sequences
# # list
# # range
# # string
# # tuple

# List comprehension - List
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]

# List comprehension - String
name = "Julio"
new_list_name = [letter for letter in name]
print(new_list_name)

# List comprehension - range
new_list_range = [number * 2 for number in range(1, 5)]
print(new_list_range)

# Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
new_list_name = [name for name in names if len(name) < 5]
print(new_list_name)

caps_name = [name.upper() for name in names if len(name) > 5]
print(caps_name)

