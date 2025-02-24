with open("./input/names/friends.txt") as names_file:
    names_list = (names_file.readlines())

with open("./input/letters/starting_letters.txt") as file:
    contents = file.read()

    for name in names_list:
        name = name.strip()
        new = contents.replace("[name]", name)
        with open(f"./output/ready_to_send/letter_for_{name}.txt", mode="w") as final_file:
            final_file.write(new)