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

# Checks that all the files in the directory are .jpeg.
def check_dir_contains_jpegs(base_dir, ill_dir):
    current_dir = os.path.join(base_dir, ill_dir)
    for files in os.walk(current_dir):
        for file in files:
            file_path = os.path.join(current_dir, file)
            if not check_file_is_jpg(file_path):
                print(f"Ensure all the files in {current_dir} are of the .jpeg file format.")
                exit()

# Creates the directories required using the images in the folder.
def create_dirs(base_dir, ill_dir):
    current_dir = os.path.join(base_dir, ill_dir)
    for files in os.walk(current_dir):
        for file in files:
            create_dir_from_image(file, current_dir)

# Generates a new directory and moves the base image to it.
def create_dir_from_image(file, current_dir, file_path):
    for key in sizes_dict:
        if file == key and key != '8x8in.jpg':
            new_dir_path = os.path.join(current_dir, sizes_dict[file][-1])
            new_file_path = os.path.join(new_dir_path, file)
            os.mkdir(new_dir_path)
            os.rename(file_path, new_file_path)

# Generates a new directory from a file name.
def create_dir_from_image(file, current_dir):
    for item in dir_list:
        if file == item[0]:
            new_dir_path = os.path.join(current_dir, item[1])
            new_file_path = os.path.join(new_dir_path, file)
            os.mkdir(new_file_path)

# Moves the images to the correct directory.
def move_images(base_dir, ill_dir):
    ill_path = os.path.join(base_dir, ill_dir)
    for files in os.walk(ill_path):
        for file in files:
            current_file_path = os.path.join(ill_path, file)
            new_file_path = os.path.join()

# == Main Code ==

# Directory creation list.
dir_list = [('4x5in.jpg', '4x5 Aspect Ratio'), ('4x6in.jpg', '2x3 Aspect Ratio'), ('5x7in.jpg', '5x7 Aspect Ratio'), ('6x8in.jpg', '3x4 Aspect Ratio'), ('11x14in.jpg', '11x14 Aspect Ratio'), ('A5.jpg', 'ISO Sizes'),
            ('5x4in.jpg', '5x4 Aspect Ratio'), ('6x4in.jpg', '3x2 Aspect Ratio'), ('7x5in.jpg', '7x5 Aspect Ratio'), ('8x6in.jpg', '4x3 Aspect Ratio'), ('14x11in.jpg', '14x11 Aspect Ratio'), ('A5.jpg', 'ISO Sizes')]

# Size list.
size_list = [
    # Portrait
    # 4x5 Aspect Ratio
    {'4x5in.jpg': [1200, 1500]}, {'8x10in.jpg': [2400, 3000]}, {'12x15in.jpg': [3600, 4500]}, {'16x20in.jpg': [4800, 6000]},
    # 2x3 Aspect Ratio
    {'4x6in.jpg': [1200, 1800]}, {'6x9in.jpg': [1800, 2700]}, {'8x12in.jpg': [2400, 3600]}, {'10x15in.jpg': [3000, 4500]}, {'12x18in.jpg': [3600, 5400]}, {'16x24in.jpg': [4800, 7200]}, {'20x30in.jpg': [6000, 9000]}, {'24x36in.jpg': [7200, 10800]},
    # 5x7 Aspect Ratio
    {'5x7in.jpg': [1500, 2100]},
    # 3x4 Aspect Ratio
    {'6x8in.jpg': [1800, 2400]}, {'9x12in.jpg': [2700, 3600]}, {'12x16in.jpg': [3600, 4800]}, {'15x20in.jpg': [4500, 6000]}, {'18x24in.jpg': [5400, 7200]},
    # 11x14 Aspect Ratio
    {'11x14in.jpg': [3300, 4200]},
    # ISO Sizes
    {'A5P.jpg': [1749, 2481]}, {'A4P.jpg': [2481, 3508]}, {'A3P.jpg': [3508, 4962]}, {'A2P.jpg': [4961, 7016]}, {'A1P.jpg': [7016, 9934]},

    # Landscape
    # 5x4 Aspect Ratio
    {'5x4in.jpg': [1500, 1200]}, {'10x8in.jpg': [3000, 2400]}, {'15x12in.jpg': [4500, 3600]}, {'20x16in.jpg': [6000, 4800]},
    # 3x2 Aspect Ratio
    {'6x4in.jpg': [1800, 1200]}, {'9x6in.jpg': [2700, 1800]}, {'12x8in.jpg': [3600, 2400]}, {'15x10in.jpg': [4500, 3000]}, {'18x12in.jpg': [5400, 3600]}, {'24x16in.jpg': [7200, 4800]}, {'30x20in.jpg': [9000, 6000]}, {'36x24in.jpg': [10800, 7200]},
    # 7x5 Aspect Ratio
    {'7x5in.jpg': [2100, 1500]},
    # 4x3 Aspect Ratio
    {'8x6in.jpg': [2400, 1800]}, {'12x9in.jpg': [3600, 2700]}, {'16x12in.jpg': [4800, 3600]}, {'20x15in.jpg': [6000, 4500]}, {'24x18in.jpg': [7200, 5400]},
    # 14x11 Aspect Ratio
    {'14x11in.jpg': [4200, 3300]},
    # ISO Sizes
    {'A5L.jpg': [2481, 1749]}, {'A4L.jpg': [3508, 2481]}, {'A3L.jpg': [4961, 3508]}, {'A2L.jpg': [7016, 4961]}, {'A1L.jpg': [9934, 7016]},

    # Square
    {'8x8in.jpg': [2400, 2400]}, {'10x10in.jpg': [3000, 3000]}, {'12x12in.jpg': [3600, 3600]}, {'16x16in.jpg': [4800, 4800]}
    ]

if has_cla() and check_cla_is_dir():
    base_dir = sys.argv[1]

# Get a list of the directories inside base_dir.
ill_dir_list = os.listdir(base_dir)

# Checks that each directory has names following the convention 'Illustration X'.
check_ill_dirs(ill_dir_list)

# Checks that each directory contains all .jpeg files.
for ill_dir in ill_dir_list:
    check_dir_contains_jpegs(base_dir, ill_dir)
    create_dirs(base_dir, ill_dir)
    move_images(base_dir, ill_dir)