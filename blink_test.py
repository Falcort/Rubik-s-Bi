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
	tmp_1 = sense.get_pixel(x, y)
	tmp_1_R = tmp_1[0]
	tmp_1_G = tmp_1[1]
	tmp_1_B = tmp_1[2]

	tmp_2 = sense.get_pixel(x+3,y)
	tmp_2_R = tmp_2[0]
	tmp_2_G = tmp_2[1]
	tmp_2_B = tmp_2[2]

	tmp_3 = sense.get_pixel(x+7,y)
	tmp_3_R = tmp_3[0]
	tmp_3_G = tmp_3[1]
	tmp_3_B = tmp_3[2]

	while i < 100:
		for j in range (8):
			sense.set_pixel(x+j, y, 0, 0, 0)
		for k in range (8):
			sense.set_pixel(x+k, y+1, 0,0,0)
		sleep(0.1)
		for m in range (8):
			if m < 1  and m < 2 :
				sense.set_pixel(x+m, y, tmp_1_R, tmp_1_G, tmp_1_B)
			elif m > 2 and m < 6 :
				sense.set_pixel(x+m, y, tmp_2_R, tmp_2_G, tmp_2_B)
			elif m > 6 and m < 9:
				sense.set_pixel(x+m, y, tmp_3_R, tmp_3_G, tmp_3_B)
			else :
				sense.set_pixel(x+m, y, 0,0,0)
		for n in range (8):
			if n < 1 and n < 2 :
				sense.set_pixel(x+n, y+1, tmp_1_R, tmp_1_G, tmp_1_B)
			elif n > 2 and n < 6 :
				sense.set_pixel(x+n, y+1, tmp_2_R, tmp_2_G, tmp_2_B)
			elif n > 6 and n < 9 :
				sense.set_pixel(x+n, y+1, tmp_3_R, tmp_3_G, tmp_3_B)
			else :
				sense.set_pixel(x+n, y+1, 0,0,0)
		sleep(0.1)
		i = i + 1
			

main()
