import os
from google.genai import types

def write_file(working_directory, file_path, content):
    joined = os.path.abspath(os.path.join(working_directory, file_path))
    
    print("Joined: ", joined)
    is_file_within = joined.startswith(os.path.abspath(working_directory))

    if is_file_within == False:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        if os.path.isfile(joined) == False:
            f = open(joined, "x")
            f.write(content)
        else:
            with open(joined, "w") as f:
                f.write(content)
    except FileNotFoundError as e: 
        raise Exception(f'Error: {e}')

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite files",
    parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
    "working_directory": types.Schema(
    type=types.Type.STRING,
    description="The file to list files from, relative to the working directory. If not provided, write files in the working directory itself.",
            ),
    "file_path": types.Schema(
    type=types.Type.STRING,
    description="The path of the file to write from."
            ),
    "content": types.Schema(
    type=types.Type.STRING,
    description="The content of the specified file"
            )
        },
    ),
)
