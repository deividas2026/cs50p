import sys
import os
from PIL import Image, ImageOps


def main():
    argc = len(sys.argv)
    if argc < 3:
        sys.exit("Too few command-line arguments")
    elif argc > 3:
        sys.exit("Too many command-line arguments")
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    image_extensions = [".jpg", ".jpeg", ".png"]
    input_file_extension = os.path.splitext(input_file)[1]
    output_file_extension = os.path.splitext(output_file)[1]
    if input_file_extension not in image_extensions:
        sys.exit("Invalid input extension") 
    elif input_file_extension != output_file_extension:
        sys.exit("Input and output have different extensions")
         
    try:
        input_image = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")
    
    shirt_image = Image.open("shirt.png")
    output_image = ImageOps.fit(input_image, shirt_image.size) 
    output_image.paste(shirt_image, (0, 0), shirt_image)
    output_image.save(output_file)
    

if __name__ == "__main__":
    main()
