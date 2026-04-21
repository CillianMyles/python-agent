from functions.get_file_content import get_file_content


def main():
    print("lorem.txt:")
    print(get_file_content("calculator", "lorem.txt"))
    print("")

    print("main.py:")
    print(get_file_content("calculator", "main.py"))
    print("")

    print("pkg/calculator.py:")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("")

    print("/bin/cat:")
    print(get_file_content("calculator", "/bin/cat"))
    print("")

    print("pkg/does_not_exist.py:")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))
    print("")


if __name__ == "__main__":
    main()
