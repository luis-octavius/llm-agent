import os
from google.genai import types


def get_file_content(working_directory, file_path):
    MAX_CHARS = 10000
    joined = os.path.abspath(os.path.join(working_directory, file_path))
    
    absolute_curr_path = os.path.abspath(working_directory)
    print("Joined: ", joined)
  
    print("Absolute Path Working Directory: ", absolute_curr_path)
    is_file_within = joined.startswith(absolute_curr_path) 
    print("Is file within: ", is_file_within)

    if is_file_within == False:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if os.path.isfile(joined) == False:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    print("Is file: ", os.path.isfile(joined))

    with open(joined, "r") as f:
        content = f.read(MAX_CHARS)

        next_char = f.read(1)
        if next_char:
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content 
        f.close()

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Get the content of the specified file.",
    parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
    "working_directory": types.Schema(
    type=types.Type.STRING,
    description="The directory which the file exists within",
            ),
    "file_path": types.Schema(
    type=types.Type.STRING,
    description="The path of the file itself"
            )
        },
    ),
)





