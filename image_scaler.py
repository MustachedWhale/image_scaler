import sys
import os
from PIL import Image

# Checks that 2 command-line arguments have been passed in.
def has_cla():
    if len(sys.argv) != 2:
        print("Provide the base folder as a command line argument.")
        exit()
    else:
        return True

# Checks that the second argument is a directory.
def check_cla_is_dir():
    if not os.path.isdir(sys.argv[1]):
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
def check_file_is_jpg(file_path):
    img = Image.open(file_path)
    if img.format == 'JPEG':
        img.close()
        return True
    else:
        img.close()
        return False

# Generates a new directory and moves the base image to it.
def create_dir_from_image(init_file, current_dir, current_file_path):
    for key in sizes_dict:
        if init_file == key and key != '8x8in.jpg':
            new_dir_path = os.path.join(current_dir, sizes_dict[file][-1])
            new_file_path = os.path.join(new_dir_path, file)
            os.mkdir(new_dir_path)
            os.rename(current_file_path, new_file_path)

# == Main Code ==

# Image size dictionaries.
sizes_dict = {
    # Portrait sizes
    '4x5in.jpg': ['8x10in.jpg', '12x15in.jpg', '16x20in.jpg', '4x5 Aspect Ratio'],
    '4x6in.jpg': ['6x9in.jpg', '8x12in.jpg', '10x15in.jpg', '12x18in.jpg', '16x24in.jpg', '20x30in.jpg', '24x36in.jpg', '2x3 Aspect Ratio'],
    '5x7in.jpg': ['5x7 Aspect Ratio'],
    '6x8in.jpg': ['9x12in.jpg', '12x16in.jpg', '15x20in.jpg', '18x24in.jpg', '3x4 Aspect Ratio'],
    '11x14in.jpg': ['11x14 Aspect Ratio'],
    'A5.jpg': ['A4.jpg', 'A3.jpg', 'A2.jpg', 'A1.jpg', 'ISO Sizes'],

    # Landscape sizes
    '5x4in.jpg': ['10x8in.jpg', '15x12in.jpg', '20x16in.jpg', '5x4 Aspect Ratio'],
    '6x4in.jpg': ['9x6in.jpg', '12x8in.jpg', '15x10in.jpg', '18.12xin.jpg', '24x16in.jpg', '30x20in.jpg', '36x24in.jpg', '3x2 Aspect Ratio'],
    '7x5in.jpg':  ['7x5 Aspect Ratio'],
    '8x6in.jpg': ['12x9in.jpg', '16x12in.jpg', '20x15in.jpg', '24x18in.jpg', '4x3 Aspect Ratio'],
    '14x11in.jpg': ['14x11 Aspect Ratio'],
    'A5.jpg': ['A4.jpg', 'A3.jpg', 'A2.jpg', 'A1.jpg', 'ISO Sizes'],
    
    # Square size
    '8x8in.jpg': ['10x10in.jpg', '12x12in.jpg', '16x16in.jpg']
}

if has_cla() and check_cla_is_dir():
    base_dir = sys.argv[1]

# Get a list of the directories inside base_dir.
illustration_dir_list = os.listdir(base_dir)

# Checks that each directory has names following the convention 'Illustration X'.
check_ill_dirs(illustration_dir_list)

# Checks whether each directory contains all jpeg files and generates the images.
for ill_dir in illustration_dir_list:
    current_dir = os.path.join(base_dir, ill_dir)
    for root, directories, files in os.walk(current_dir):
        for file in files:
            current_file_path = os.path.join(current_dir, file)
            if check_file_is_jpg(current_file_path):
                create_dir_from_image(file, current_dir, current_file_path)
            else:
                print(f"Ensure all the files in {current_dir} are of the .jpeg file format.")
                exit()