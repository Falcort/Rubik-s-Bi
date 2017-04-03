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

sense.set_pixels(image)
direction = 2
number = 1
if direction == 2 or direction == 1:
    for i in range(0,7):
        if number == 1:
            for j in range(0,1):
                tmp1=sense.get_pixel(i,j)
                sense.set_pixel(i,j,w)
                if i == 2 or i == 5:
                    i=i+1
        elif number == 2:
            for j in range(3,4):
                tmp2=sense.get_pixel(i,j)
                sense.set_pixel(i,j,w)
            if i==2 or i==5:
                i=i+1
        elif number == 3:
            for j in range(6,7):
                tmp3=sense.get_pixel(i,j)
                sense.set_pixel(i,j,w)
            if i==2 or i==5:
                i=i+1

else:
    for j in range(0,7):
        if number == 1:
            for i in range(0,1):
                tmp1=sense.get_pixel(i,j)
                sense.set_pixel(i,j,w)
            if j == 2 or j == 5:
                j=j+1
        elif number == 2:
            for i in range(3,4):
                tmp2=sense.get_pixel(i,j)
                sense.get_pixel(i,j,w)
            if j==2 or j==5:
                j=j+1
        elif number == 3 :
            for i in range(6,7):
                tmp3=sense.get_pixel(i,j)
                sense.set_pixel(i,j,w)
            if j==2 or j==5:
                j=j+1


for i in range (0,7):
    if number == 1:
        for j in range(0,1):
            sense.set_pixel(i,j,tmp1)
        if i == 2 or i == 5:
            i=i+1
    elif number == 2:
        for j in range(3,4):
            sense.set_pixel(i,j,tmp2)
        if i==2 or i==5:
            i=i+1
    elif number == 3:
        for j in range(6,7):
            sense.set_pixel(i,j,tmp3)
        if i==2 or i==5:
            i=i+1
for j in range(0,7):
    if number == 1:
        for i in range(0,1):
            sense.set_pixel(i,j,tmp1)
        if j == 2 or j == 5:
            j=j+1
    elif number == 2:
        for i in range(3,4):
            sense.set_pixel(i,j,tmp2)
        if j==2 or j==5:
            j=j+1
    elif number == 3:
        for i in range(6,7):
            sense.set_pixel(i,j,tmp3)
        if j==2 or j==5:
            j=j+1
