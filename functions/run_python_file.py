import os


def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
    except Exception as e:
        return f"Error: Failed to run python file: {e}"
