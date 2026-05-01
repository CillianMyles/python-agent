from google.genai.types import Tool

from functions.list_files import schema_list_files
from functions.read_file import schema_read_file
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file


available_functions = Tool(
    function_declarations=[
        schema_list_files,
        schema_read_file,
        schema_write_file,
        schema_run_python_file,
    ],
)
