import random

def select_name_from_file(filename: str) -> str:
    with open(filename, "r+") as file:
        names: list = file.read()

    selected_name = random.choice(names)
    return selected_name


def select_name_from_list(names: tuple) -> str:
    selected_name = random.choice(names)
    return selected_name
