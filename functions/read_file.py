import os

from config import MAX_CHARS


def read_file(working_directory, file_path):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))
        print(f"working: {abs_working_dir}")
        print(f"target: {target_file}")

        if os.path.commonpath([abs_working_dir, target_file]) != abs_working_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(target_file):
            return f'Error: File not found: "{file_path}"'

        if not os.path.isfile(target_file):
            return f'Error: Not a regular file: "{file_path}"'

        contents = ""
        with open(target_file, "r") as f:
            contents = f.read(MAX_CHARS)
            if f.read(1):
                contents += f'[...File "{file_path}" at {MAX_CHARS} characters]'
        return contents

    except Exception as e:
        return f"Error: reading file: {e}"
