import os


def write_file(working_directory, file_path, content):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))

        if os.path.commonpath([abs_working_dir, target_file]) != abs_working_dir:
            return f'Error: Cannot edit outside the permitted working directory: "{file_path}"'

        if not os.path.exists(target_file):
            return f'Error: File not found: "{file_path}"'
        
        if os.path.isdir(target_file):
            return f'Error: Actually a directory: "{file_path}"'

        if not os.path.isfile(target_file):
            return f'Error: Not a regular file: "{file_path}"'

    except Exception as e:
        return f"Error: Failed to write file: {e}"
