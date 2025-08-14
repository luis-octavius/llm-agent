from functions.get_files_info import get_files_info 
from functions.get_file_content import get_file_content 
from functions.write_file import write_file 
from functions.run_python_file import run_python_file 

def print_get_files(func):
#     if dir == ".":
#         print(f"""
# Result for current directory:
# {func}
#         """)
#     else:
    print(f"""
{func}
""")

test1 = run_python_file("calculator", "main.py")
print_get_files(test1)

test2 = run_python_file("calculator", "main.py", "[3 + 5]")
print_get_files(test2)

test3 = run_python_file("calculator", "../main.py")
print_get_files(test3)

test4 = run_python_file("calculator", "nonexistent.py")
print_get_files(test4)











