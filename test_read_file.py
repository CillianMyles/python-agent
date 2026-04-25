from functions.read_file import read_file


def main():
    print("lorem.txt:")
    print(read_file("calculator", "lorem.txt"))
    print("")

    print("main.py:")
    print(read_file("calculator", "main.py"))
    print("")

    print("pkg/calculator.py:")
    print(read_file("calculator", "pkg/calculator.py"))
    print("")

    print("/bin/cat")
    print(read_file("calculator", "/bin/cat"))
    print("")

    print("pkg/does_not_exist.py")
    print(read_file("calculator", "pkg/does_not_exist.py"))
    print("")


if __name__ == "__main__":
    main()
