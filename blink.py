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
g,g,w,w,w,w,g,g,
g,g,w,w,w,w,g,g,
w,w,w,w,w,w,w,w,
r,r,w,r,r,w,r,r,
r,r,w,r,r,w,r,r,
w,w,w,w,w,w,w,w,
r,r,w,r,r,w,r,r,
r,r,w,r,r,w,r,r
]

