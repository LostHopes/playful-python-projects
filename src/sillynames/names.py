import random

def from_file(filename: str) -> str:
    """Reads names from the list of given file"""

    with open(filename, "r+") as file:
        names: list = file.read()

    selected_name = random.choice(names)
    return selected_name


def from_list(names: tuple | list) -> str:
    selected_name = random.choice(names)
    return selected_name
