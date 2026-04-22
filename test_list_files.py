from functions.list_files import list_files


def main():
    print("Current directory:")
    print(list_files("calculator", "."))
    print("")

    print("'pkg' directory:")
    print(list_files("calculator", "pkg"))
    print("")

    print("'/bin' directory:")
    print(list_files("calculator", "/bin"))
    print("")

    print("'../' directory:")
    print(list_files("calculator", "../"))
    print("")


if __name__ == "__main__":
    main()
