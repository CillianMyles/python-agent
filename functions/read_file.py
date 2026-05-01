import os

from google.genai.types import FunctionDeclaration, Schema, Type

from config import MAX_CHARS


def read_file(working_directory, file_path):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))

        if os.path.commonpath([abs_working_dir, target_file]) != abs_working_dir:
            return f'Error: Cannot read outside the permitted working directory: "{file_path}"'

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
        return f"Error: Failed to read file: {e}"


schema_read_file = FunctionDeclaration(
    name="read_file",
    description="Read the contents of a specified file",
    parameters=Schema(
        type=Type.OBJECT,
        properties={
            "file_path": Schema(
                type=Type.STRING,
                description="Path to the file to be read, relative to the current working directory",
            ),
        },
    ),
)
