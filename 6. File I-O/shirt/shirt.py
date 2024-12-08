import sys
import os
from PIL import Image, ImageOps

ext1 = os.path.splitext(sys.argv[1])
ext2 = os.path.splitext(sys.argv[2])

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if ext1[1] not in [".jpg", ".png"] or ext2[1] not in [".jpg", ".png"]:
    sys.exit("Invalid input")
if ext1[1] != ext2[1]:
    sys.exit("Input and output have different extensions")
else:
    try:
        shirt = Image.open("shirt.png")
        size = shirt.size
        with Image.open(sys.argv[1]) as input:
            resized_input = ImageOps.fit(input, size)
            resized_input.paste(shirt, shirt)
            resized_input.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("File does not exist")
