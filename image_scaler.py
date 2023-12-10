import sys
import os
from PIL import Image

# Checks that 2 command-line arguments have been passed in and that the second argument is a directory.
def check_cla_is_dir():
    if len(sys.argv) != 2 or not os.path.isdir(sys.argv[1]):
        print("Provide the base folder as a command line argument.")
        exit()
    else:
        return True

# Checks each folder name follows the convention 'Illustration X'.    
def check_ill_dirs(illustration_dir_list):
    for d in illustration_dir_list:
        if 'Illustration' in d and d[-1].isnumeric():
            continue
        else:
            print("Ensure that all subdirectories are named in the convention 'Illustration X', where X is a number.")
            exit()

# == Main Code ==

if check_cla_is_dir():
    base_dir = sys.argv[1]

# Get a list of the directories inside base_dir.
illustration_dir_list = os.listdir(base_dir)

# Checks that each directory has names following the convention 'Illustration X'.
check_ill_dirs(illustration_dir_list)

# Checks whether each directory contains all jpeg files.
for current_dir in illustration_dir_list:
    # Check that each file in the directory is a .jpg file.
    for root, directories, files in os.walk(current_dir):
        for file in files:
            img = Image.open(file)
            if img.format == 'JPEG':
                continue
            else:
                print(f"Ensure that all the files in {current_dir} are of the .jpg file format.")