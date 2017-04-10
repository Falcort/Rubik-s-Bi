from sense_hat import SenseHat

sense = SenseHat()

while True:
    orientation = sense.get_orientation()
    pitch = orientation['pitch']
    roll = orientation['roll']
    yaw = orientation['yaw']
    print("pitch={0}, roll={1}, yaw={2}".format(pitch,roll,yaw))
    
    r = [255,0,0]
    b = [0,0,255]
    g = [0,255,0]
    y = [255,215,0]
    p = [205,0,255]

    if ( pitch>=225 and pitch<=315) :
                
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
        
    if (( (pitch>=0 and pitch<=45) or (pitch>=315 and pitch<=360) )  ) :
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
        
    if (pitch>=45 and pitch<=135) :
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

    if ((roll>=45 and roll<=135) ) :
        image = [
        y,y,y,y,y,y,y,y,
        y,y,y,y,y,y,y,y,
        y,y,y,y,y,y,y,y,
        y,y,y,y,y,y,y,y,
        y,y,y,y,y,y,y,y,
        y,y,y,y,y,y,y,y,
        y,y,y,y,y,y,y,y,
        y,y,y,y,y,y,y,y,
        ]
        sense.set_pixels(image)

    if ((roll>=225 and roll<=315) and ((pitch>=0 and pitch<=45) or (pitch>=315 and pitch<=360) )) :
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
        

sense.clear()
