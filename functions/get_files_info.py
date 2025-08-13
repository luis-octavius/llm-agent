import os

def get_files_info(working_directory, directory="."):

    joined_path = os.path.abspath(os.path.join(working_directory, directory))

    print("Joined Path: ", joined_path)
    
    is_directory_within = joined_path.startswith(os.path.abspath(working_directory))

    print("Is directory within: ", is_directory_within)
    
    if is_directory_within == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if os.path.isdir(joined_path) == False:
        return f'Error: "{directory}" is not a directory'
    
    dir_content = get_dir_content(joined_path)
    print(f"Dir Content: \n{dir_content}")

    return dir_content


def get_dir_content(dir):
    dir_list = os.listdir(dir)
    print(dir_list)
    
    files_list = []

    for file in dir_list:
        file_path = os.path.join(dir, file)
        print("File path: ", file_path)

        is_dir = os.path.isdir(file_path)
        file_size = os.path.getsize(file_path)

        file_str = f"- {file}: file_size={file_size}, is_dir={is_dir}"
        files_list.append(file_str)

    return "\n".join(files_list)



