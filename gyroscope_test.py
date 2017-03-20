from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

sense.show_letter("J", text_colour=[0,255,0])

r = [255,0,0]
g = [0,255,0]
b = [0,0,255]


while True :
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = round(x,0)
    y = round(y,0)
    z = round(z,0)

    if (x == -1) :
        image = [
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        ]
        sense.set_pixels(image)
        
    elif (y == 1) :
        image = [
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        ]
        sense.set_pixels(image)
        
    elif (y == -1):
        sense.set_rotation(270)
    else :
        sense.set_rotation(0)



sleep(10)        


sense.clear()
