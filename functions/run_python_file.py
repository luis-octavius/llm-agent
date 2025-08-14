import os 
import subprocess
import sys

def run_python_file(working_directory, file_path, args=[]):

    joined = os.path.abspath(os.path.join(working_directory, file_path))

    print("Joined: ", joined)
    is_file_within = joined.startswith(os.path.abspath(working_directory))

    print("Is file within", is_file_within)

    if is_file_within == False:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if os.path.isfile(joined) == False:
        return f'Error: File "{file_path}" not found.'

    if joined.endswith('.py') == False:
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run([sys.executable, f"{joined}", *args], timeout=30, capture_output=True, check=True)

        print("Result stdout: ", result.stdout)
        print("Result stderr: ", result.stderr)

        print(f"""
STDOUT: {result.stdout}
STDERR: {result.stderr}
    """)

        if result.check_returncode() != 0:
            raise(f'Process exited with code {result.returncode}')
        if result.stdout == None:
            return f"No output produced"
        print("Result ")
    except Exception as e:
        print(f'Error: executing Python file: {e}')


