from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()
r = [255,0,0]
g = [0,255,0]
b = [0,0,255]
w = [0,0,0]
p = [255,0,255]
gb = [0,255,255]
rg = [255,255,0]

image = [
r,r,w,p,p,w,r,r,
r,r,w,p,p,w,r,r,
w,w,w,w,w,w,w,w,
g,g,w,gb,gb,w,g,g,
g,g,w,gb,gb,w,g,g,
w,w,w,w,w,w,w,w,
b,b,w,rg,rg,w,b,b,
b,b,w,rg,rg,w,b,b
]

sense.set_pixels(image)

angles = [0,90,180,270, 0, 90, 180, 270]
for r in angles:
    sense.set_rotation(r)
    sleep(0.5)

















