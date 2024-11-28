import os
import subprocess
import sys

# Function to install a package using pip
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Check and install required packages
required_packages = ["fonttools", "brotli"]
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        install_package(package)

from fontTools.ttLib import TTFont

def get_font_info(font_path):
    font = TTFont(font_path)
    name = ""
    style = ""
    for record in font['name'].names:
        if record.nameID == 1:
            name = record.toUnicode()
        elif record.nameID == 2:
            style = record.toUnicode()
    return name, style

# Get the current directory
font_directory = os.getcwd()

# Get all font files in the current directory
font_files = [f for f in os.listdir(font_directory) if f.endswith(('.ttf', '.woff', '.woff2', '.otf'))]

# Loop through each font file and rename it
for font_file in font_files:
    font_path = os.path.join(font_directory, font_file)
    try:
        name, style = get_font_info(font_path)
        new_file_name = f"{name}-{style}{os.path.splitext(font_file)[1]}"
        new_file_path = os.path.join(font_directory, new_file_name)
        os.rename(font_path, new_file_path)
        print(f"Renamed {font_file} to {new_file_name}")
    except Exception as e:
        print(f"Failed to process {font_file}: {e}")
