"""CS 108 - Homework 4

This module runs a command-line interface that controls successive image
processing commands. The image is redisplayed after each command.

@author: Keith VanderLinden (kvlinden) and Ken Arnold (ka37) 
@date: Spring, 2020

@author: Alex Miller (ajm94)
@date: Fall, 2021
"""

from image_processing import *


MENU = 'b - Brighten' \
       '\nfh - Flip Horizontal' \
       '\nd - Darken' \
       '\nn - Negative' \
       '\ngs - Gray Scale' \
       '\nfv - Flip Vertical' \
       '\nsn - Snow' \
       '\nsp - Sepia' \
       '\np - Polarize' \
       '\nq - Quit'

image = load_image('images/sydney_sunset.png')

# Run a CLI loop, allowing the user to repeat commands by hitting enter.
previous_command = ''
while True:
    print('Close the image window to proceed.')
    display_image(image)
    print(MENU)
    command = input('Command: ').lower()

    if command == '':
        command = previous_command

    if command == 'b':
        image = change_brightness(image, 25)
    elif command == 'fh':
        image = flip_horizontal(image)
    elif command == 'd':
        image = change_brightness(image, -25)
    elif command == 'n':
        image = negative(image)
    elif command == 'gs':
        image = gray_scale(image)
    elif command == 'fv':
        image = flip_vertical(image)
    elif command == 'sn':
        image = snow(image)
    elif command == 'sp':
        image = sepia(image)
    elif command == 'p':
        image = polarize(image)
    elif command == 'q':
        break
    else:
        print('invalid command')

    previous_command = command
