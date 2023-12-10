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

# Checks that a file is of the .jpg file type.
def check_file_is_jpg():
    img = Image.open(file)
    if img.format == 'JPEG':
        img.close()
    else:
        print(f"Ensure that all the files in {current_dir} are of the .jpg file format.")
        img.close()
        exit()

# Generates a new directory and images based on the name of the initial file.
def generate_new_images(init_file):
    pass

# == Main Code ==

# Image size dictionaries.
portrait_sizes_dict = {
    '4x5in.jpg':    [],
    '4x6in.jpg':    [],
    '5x7in.jpg':    [],
    '6x8in.jpg':    [],
    '11x14in.jpg':  [],
    'A5.jpg':       []
}
landscape_sizes_dict = {

}
square_sizes_dict = {

}

if check_cla_is_dir():
    base_dir = sys.argv[1]

# Get a list of the directories inside base_dir.
illustration_dir_list = os.listdir(base_dir)

# Checks that each directory has names following the convention 'Illustration X'.
check_ill_dirs(illustration_dir_list)

# Checks whether each directory contains all jpeg files.
for current_dir in illustration_dir_list:
    for root, directories, files in os.walk(current_dir):
        for file in files:
            check_file_is_jpg()
            generate_new_images(file)