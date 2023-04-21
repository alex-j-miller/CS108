"""CS 108 - Lab 4.1

Wind Chill

@author: Alex Miller (ajm94)
@date: Fall, 2021
"""
#Get initial values
temp = float(input('Temperature: '))
w_speed = float(input('Wind speed: '))

#check the region
if w_speed < 2 or temp < -58 or temp > 41:
    print('Invalid input')
else:
    #calculate wind chill
    w_chill = 35.74 + (0.6215 * temp) - (35.75 * (w_speed ** 0.16)) + (0.4275 * temp * (w_speed ** 0.16))

    #find the number of layers
    if w_chill < -40:
        layers = 'Stay home!'
    elif w_chill < -10:
        layers = 'Four layers'
    elif w_chill < 20:
        layers = 'Three layers'
    elif w_chill < 40:
        layers = 'Two layers'
    elif w_chill >= 40:
        layers = 'One layer'

    #print out final results
    print('Wind chill:', w_chill)
    print(layers)