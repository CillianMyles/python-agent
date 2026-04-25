import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))

        if os.path.commonpath([abs_working_dir, target_file]) != abs_working_dir:
            return f'Error: Cannot run file outside the permitted working directory: "{file_path}"'

        if not os.path.exists(target_file):
            return f'Error: File not found: "{file_path}"'

        if not os.path.isfile(target_file):
            return f'Error: Not a regular file: "{file_path}"'

        if not file_path.endswith(".py"):
            return f'Error: Not a python file: "{file_path}"'

        command = ["python", file_path]
        if args:
            command.extend(args)

        process = subprocess.run(
            command,
            cwd=working_directory,
            capture_output=True,
            text=True,
            timeout=30,
        )

        if process.returncode != 0:
            return f"Error: Non-zero return code: {process.returncode}"

        if not process.stdout and not process.stderr:
            return f"Error: No output produced"

        return f"---\nSTDOUT: {process.stdout.strip()}\n---\nSTDERR: {process.stderr.strip()}"

    except Exception as e:
        return f"Error: Failed to run python file: {e}"
