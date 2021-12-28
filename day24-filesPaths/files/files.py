# #Open file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# #Write file
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

# # if the file do not exist will be created
with open("new_file.txt", mode="a") as file:
    file.write("\nNew text.")
