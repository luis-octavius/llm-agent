import os

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


