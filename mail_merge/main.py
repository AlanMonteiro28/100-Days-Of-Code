list_names = []

with open("./Input/Names/invited_names.txt") as data_names:
    names = data_names.readlines()

with open("./Input/Letters/starting_letter.txt") as data_letter:
    letter = data_letter.read()

for n in names:
    stripped_names = n.strip("\n")
    list_names.append(stripped_names)

for name in list_names:
    new_letter = letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as data_letters:
        data_letters.write(new_letter)
