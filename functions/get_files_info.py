import os


def get_files_info(working_directory, directory="."):
    working = os.path.abspath(working_directory)
    target = os.path.join(working, directory)
    normalized = os.path.normpath(target)
    print("-" * 20)
    print(f"working: {working}")
    print(f"target: {target}")
    print(f"normalized: {normalized}")


if __name__ == "__main__":
    get_files_info(".")
    get_files_info("calculator")
    get_files_info("functions")
