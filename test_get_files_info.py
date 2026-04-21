from functions.get_files_info import get_files_info


def main():
    print("Current directory:")
    print(get_files_info("calculator", "."))
    print("")

    print("'pkg' directory:")
    print(get_files_info("calculator", "pkg"))
    print("")

    print("'/bin' directory:")
    print(get_files_info("calculator", "/bin"))
    print("")

    print("'../' directory:")
    print(get_files_info("calculator", "../"))
    print("")


if __name__ == "__main__":
    main()
