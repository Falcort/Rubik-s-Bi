from sense_hat import SenseHat
from time import sleep

sense = SenseHat()


while True :
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = round(x,0)
    y = round(y,0)
    z = round(z,0)

    p = [255,69,0]
    r = [255,0,0]
    g = [0,255,0]
    b = [0,0,255]
    f = [255,255,0]
    
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

    elif (y == -1) :
        image = [
        f,f,f,f,f,f,f,f,
        f,f,f,f,f,f,f,f,
        f,f,f,f,f,f,f,f,
        f,f,f,f,f,f,f,f,
        f,f,f,f,f,f,f,f,
        f,f,f,f,f,f,f,f,
        f,f,f,f,f,f,f,f,
        f,f,f,f,f,f,f,f,
        ]
        sense.set_pixels(image)


    elif (x == 1) :
        image = [
        p,p,p,p,p,p,p,p,
        p,p,p,p,p,p,p,p,
        p,p,p,p,p,p,p,p,
        p,p,p,p,p,p,p,p,
        p,p,p,p,p,p,p,p,
        p,p,p,p,p,p,p,p,
        p,p,p,p,p,p,p,p,
        p,p,p,p,p,p,p,p,
        ]
        sense.set_pixels(image)
        
    elif (x == 0) :
        image = [
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        ]
        sense.set_pixels(image)

    else :
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



sleep(10)        


sense.clear()
