import os


def get_files_info(working_directory, directory="."):
    working_path = os.path.abspath(working_directory)
    directory_path = os.path.abspath(directory)
    print(f"working_path: {working_path}")
    print(f"directory_path: {directory_path}")


if __name__ == "__main__":
    get_files_info("calculator")
