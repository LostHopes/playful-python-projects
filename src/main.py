from silly import names


def main() -> None:
    firstnames: tuple = ("Cucumber", "Toes")
    surnames: tuple = ("Cocka", "Buka")

    name: str = names.from_list(firstnames)
    surname: str = names.from_list(surnames)

    print(f"{name} {surname}")
    

if __name__ == "__main__":
    main()