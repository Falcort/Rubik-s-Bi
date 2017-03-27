from sense_hat import SenseHat

sense = SenseHat()

while True:
    orientation = sense.get_orientation()
    pitch = orientation['pitch']
    roll = orientation['roll']
    yaw = orientation['yaw']
    #print("pitch={0}, roll={1}, yaw={2}".format(pitch,yaw,roll))
    
    r = [255,0,0]
    b = [0,0,255]

    if ((pitch>=0 and pitch<=60)or(pitch>=300 and pitch<=360)) :
                
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
    elif ((pitch<=300 and pitch<=270) :
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
        

sense.clear()
