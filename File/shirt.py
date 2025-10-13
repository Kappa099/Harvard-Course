import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) != 3:
    sys.exit("Usage: python shirt.py input.(jpg|jpeg|png) output.(jpg|jpeg|png)")

input_file = sys.argv[1]
output_file = sys.argv[2]

valid_extensions = [".jpg", ".jpeg", ".png"]

in_ext = os.path.splitext(input_file)[1].lower()
out_ext = os.path.splitext(output_file)[1].lower()

if in_ext not in valid_extensions or out_ext not in valid_extensions:
    sys.exit("Input and output must be .jpg, .jpeg, or .png")

if in_ext != out_ext:
    sys.exit("Input and output have different extensions")

try:
    photo = Image.open(input_file)
except FileNotFoundError:
    sys.exit("Input file does not exist")

shirt = Image.open("shirt.png")

size = shirt.size
photo = ImageOps.fit(photo, size)

photo.paste(shirt, shirt)

photo.save(output_file)