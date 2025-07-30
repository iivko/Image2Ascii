"""
    Image to ASCII @, #, $, O, ?, *, +, ;, .
"""


from PIL import Image
import numpy as np


ascii_chars = "@#$O?*+;."

def img_rgb_2_gray(image_path: str):
    """
        Tranforms RGB image to grayscale image
    """
    return Image.open(image_path).convert("L")


def resizing_image(new_width, img):
    """
        This function resizes the image
    """
    w_percent = new_width / float(img.size[0])
    h_size = int(float(img.size[1]) * w_percent)

    resized_img = img.resize((new_width, h_size), Image.LANCZOS)
    # resized_img = resized_img.rotate(270)

    return resized_img


def image_to_ascii_array(img):
    """
        This function creates the ascii array
    """
    img_ascii = []
    scale = 255 // (len(ascii_chars) - 1)

    img_pixels = np.array(img)

    for idx, pixel_row in enumerate(img_pixels):
        img_ascii.append([])
        for pixel in pixel_row:
            if pixel >= 245:
                img_ascii[idx].append(" ")

            else:
                img_ascii[idx].append(ascii_chars[pixel // scale])

    return img_ascii


def write_ascii_to_file(ascii_image) -> None:
    """
        This function writes the image to a text file
    """
    with open("ascii.txt", "w") as out:
        for row in ascii_image:
            for char in row:
                out.write(char)
            out.write("\n")


def convert(image_path: str, resize: int = 100) -> None:
    img = img_rgb_2_gray(image_path)
    resized_img = resizing_image(resize, img)
    ascii_array = image_to_ascii_array(resized_img)
    write_ascii_to_file(ascii_array)


if __name__ == "__main__":
    convert("3d-view-skull.jpg")