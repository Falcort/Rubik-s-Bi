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

def main():
	sense.set_pixels(image)
	blink(0,0)


def blink(x, y):
	i = 0
	tmp = sense.get_pixel(x, y)
	tmp_R = tmp[0]
	tmp_G = tmp[1]
	tmp_B = tmp[2]
	while i < 100:
		for i in range (8):
			sense.set_pixel(x+i, y, 0, 0, 0)
		for i in range (8):
			sense.set_pixel(x, y+i, 0,0,0)
		sleep(0.1)
		for i in range (8):
			sense.set_pixel(x+i, y, tmp_R, tmp_G, tmp_B)
		for i in range (8):
			sense.set_pixel(x, y+i, tmp_R, tmp_G, tmp_B)
		sleep(0.1)
		i = i + 1

main()

