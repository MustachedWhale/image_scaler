import sys
import os

# Checks that 2 command-line arguments have been passed in and that the second argument is a directory.
def check_cla():
    if len(sys.argv) != 2 or not os.path.isdir(sys.argv[1]):
        print("Provide the base folder as a command line argument.")
        exit()
    else:
        return True
    
def check_ill_dirs(illustration_dir_list):
    for d in illustration_dir_list:
        if 'Illustration' in d and d[-1].isnumeric():
            continue
        else:
            print("Ensure that all subdirectories are named in the convention 'Illustration X', where X is a number.")
            exit()

# == Main Code ==

if check_cla():
    base_dir = sys.argv[1]

# Get a list of the directories inside base_dir.
illustration_dir_list = os.listdir(base_dir)

# Checks that each directory has names following the convention 'Illustration X'.
check_ill_dirs(illustration_dir_list)