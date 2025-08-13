from functions.get_files_info import get_files_info 

def print_get_files(func, dir):
    if dir == ".":
        print(f"""
Result for current directory:
{func}
        """)
    else:
        print(f"""
Result for '{dir}' directory:
{func}
        """)

# test one 
calculator_test = get_files_info("calculator", ".")

print_get_files(calculator_test, ".")

# test two
pkg_test = get_files_info("calculator", "pkg")
print_get_files(pkg_test, "pkg")

# test three
bin_test = get_files_info("calculator", "/bin")
print_get_files(bin_test, "/bin")

# test four 
out_test = get_files_info("calculator", "../")
print_get_files(out_test, "../")















