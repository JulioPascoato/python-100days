with open("./Input/Names/invited_names.txt", "r") as invited_names:
    names = invited_names.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as starting_letter:
    starting_letter_content = starting_letter.read()

for name in names:
    new_letter = starting_letter_content.replace("[name]", name.rstrip())
    file_name = f"letter_for_{name.rstrip()}.txt"
    with open(f"./Output/ReadyToSend/{file_name}", mode="w") as file:
        file.write(new_letter)


