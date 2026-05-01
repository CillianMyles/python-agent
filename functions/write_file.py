import os

from google.genai.types import FunctionDeclaration, Schema, Type


def write_file(working_directory, file_path, content):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))

        if os.path.commonpath([abs_working_dir, target_file]) != abs_working_dir:
            return f'Error: Cannot write outside the permitted working directory: "{file_path}"'

        if os.path.isdir(target_file):
            return f'Error: Cannot write to file that is a directory: "{file_path}"'

        parent_dir = os.path.dirname(target_file)
        os.makedirs(parent_dir, exist_ok=True)

        with open(target_file, "w") as f:
            f.write(content)

        return f"Successfully wrote to {file_path} ({len(content)} characters written)"

    except Exception as e:
        return f"Error: Failed to write file: {e}"


schema_write_file = FunctionDeclaration(
    name="write_file",
    description="Write the given contents to a specified file",
    parameters=Schema(
        type=Type.OBJECT,
        properties={
            "file_path": Schema(
                type=Type.STRING,
                description="Path to the file to be written, relative to the current working directory",
            ),
            "content": Schema(
                type=Type.STRING,
                description="Contents to be written to the file",
            ),
        },
    ),
)
