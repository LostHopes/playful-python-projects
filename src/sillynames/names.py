import random

def select_name_from_file(filename: str) -> str:
    with open(filename, "r+") as file:
        names: list = file.read()

    selected_name = random.choice(names)
    return selected_name


def select_name_from_list(names: list) -> str:
    selected_name = random.choice(names)
    return selected_name
