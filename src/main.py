from sillynames.names import select_name_from_list


def main() -> None:
    firstnames: list = ["Cucumber", "Toes"]
    surnames: list = ["Cocka", "Buka"]

    name: str = select_name_from_list(firstnames)
    surname: str = select_name_from_list(surnames)

    print(f"{name} {surname}")
    

if __name__ == "__main__":
    main()