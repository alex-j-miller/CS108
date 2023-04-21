"""CS 108 - Lab 8

This module implements image processing functions using the Python Imaging
Library (PIL) to load and display images, and NumPy to manipulate the image's
2D array of pixels. Each pixel is represented as a list of intensity values
for red, green and blue (RGB), each value between 0 (low intensity) and 255 (
high intensity). For example:
    [0, 0, 0] represents black
    [255, 255, 255] represents white
    [255, 0, 0] represents red

@author: Keith VanderLinden (kvlinden) and Ken Arnold (ka37)
@date: Spring, 2020 - ported from Java/Processing, Fall, 2010

@author: Alex Miller (ajm94)
@date: Fall, 2021
"""


from PIL import Image
import random
import numpy as np
from copy import deepcopy
from guizero import App, Picture


def load_image(filename):
    """ This function loads an image from the specified file. """

    # Convert pixel values to integer format in order to
    # allow arithmetic that may overflow np's default uint8.
    return np.array(Image.open(filename), dtype='int32')


def display_image(image_array):
    """ This function displays the given image in a separate GuiZero window. """

    # Clip pixel values back to 8-bit range for display.
    image = Image.fromarray(np.uint8(np.clip(image_array, 0, 255)))

    # Show the image in a guizero window.
    app = App(width=image_array.shape[1], height=image_array.shape[0])
    Picture(app, image=image)
    # Bring the guizero window to the front
    # https://stackoverflow.com/a/36191443/69707
    root = app.tk
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    app.display()

def flip_horizontal(image):
    """ This function mirrors the given image around a vertical line. """

    # Why is this operation needed?
    # You will replace pixels that you will need in the future.
    image_copy = deepcopy(image)

    num_rows = len(image)
    num_columns = len(image[0])

    for row_index in range(num_rows):
        for column_index in range(num_columns):
            image[row_index][column_index] = image_copy[row_index][num_columns - column_index - 1]

    return image

def change_brightness(image, mag):
    ''' This function makes the given image change brightness '''
        
    num_rows = len(image)
    num_columns = len(image[0])

    # Change the value each RGB pixel.
    for row_index in range(num_rows):
        for column_index in range(num_columns):
            rgb = image[row_index][column_index]
            image[row_index][column_index] = [
                rgb[0] + int(mag),
                rgb[1] + int(mag),
                rgb[2] + int(mag)
            ]

    return image

def negative(image):
    ''' This function makes the given image a negetive of itself '''
    
    num_rows = len(image)
    num_columns = len(image[0])

    # Change the value each RGB pixel.
    for row_index in range(num_rows):
        for column_index in range(num_columns):
            rgb = image[row_index][column_index]
            image[row_index][column_index] = [
                255 - rgb[0] ,
                255 - rgb[1] ,
                255 - rgb[2]
            ]

    return image

def gray_scale(image):
    ''' This function makes the given image a gray scale of itself '''
    
    num_rows = len(image)
    num_columns = len(image[0])

    # Change the value each RGB pixel.
    for row_index in range(num_rows):
        for column_index in range(num_columns):
            rgb = image[row_index][column_index]
            avg_val = (rgb[0] + rgb[1] + rgb[2]) // 3
            image[row_index][column_index] = [
                avg_val,
                avg_val,
                avg_val
            ]

    return image

def flip_vertical(image):
    """ This function mirrors the given image around a horizontal line. """
    
    image_copy = deepcopy(image)

    num_rows = len(image)
    num_columns = len(image[0])

    for row_index in range(num_rows):
        image[row_index] = image_copy[num_rows - row_index - 1]

    return image

def snow(image):
    ''' This function produces visual noise '''
    
    num_rows = len(image)
    num_columns = len(image[0])
    
    for row_index in range(num_rows):
        for column_index in range(num_columns):
            image[row_index][column_index] = [
                random.randint(0,255),
                random.randint(0,255),
                random.randint(0,255)
                ]
    