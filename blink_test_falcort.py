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
g,g,w,b,b,w,r,r,
g,g,w,b,b,w,r,r,
w,w,w,w,w,w,w,w,
r,r,w,r,r,w,r,r,
r,r,w,r,r,w,r,r,
w,w,w,w,w,w,w,w,
b,b,w,r,r,w,r,r,
b,b,w,r,r,w,r,r
]

def main():
	sense.set_pixels(image)
	blinkLine(0)
	blinkLine(3)
	blinkLine(6)
	blinkRow(0)
	blinkRow(3)
	blinkRow(6)


def blinkLine(x):
	a=0
	for i in range (8):
		if(i==0):
			tmp_1 = sense.get_pixel(x, i);
			tmp_1_R = tmp_1[0]
			tmp_1_G = tmp_1[1]
			tmp_1_B = tmp_1[2]
		if(i==3):
			tmp_2 = sense.get_pixel(x,i)
			tmp_2_R = tmp_2[0]
			tmp_2_G = tmp_2[1]
			tmp_2_B = tmp_2[2]
		if(i==6):
			tmp_3 = sense.get_pixel(x,i)
			tmp_3_R = tmp_3[0]
			tmp_3_G = tmp_3[1]
			tmp_3_B = tmp_3[2]

	while a<10:
		sense.set_pixel(x, 0, 0, 0, 0);
		sense.set_pixel(x, 1, 0, 0, 0);
		sense.set_pixel(x+1, 0, 0, 0, 0);
		sense.set_pixel(x+1, 1, 0, 0, 0);

		sense.set_pixel(x, 3, 0, 0, 0);
		sense.set_pixel(x, 4, 0, 0, 0);
		sense.set_pixel(x+1, 3, 0, 0, 0);
		sense.set_pixel(x+1, 4, 0, 0, 0);

		sense.set_pixel(x, 6, 0, 0, 0);
		sense.set_pixel(x, 7, 0, 0, 0);
		sense.set_pixel(x+1, 6, 0, 0, 0);
		sense.set_pixel(x+1, 7, 0, 0, 0);
		sleep(0.1)
		sense.set_pixel(x, 0, tmp_1_R, tmp_1_G, tmp_1_B);
		sense.set_pixel(x, 1, tmp_1_R, tmp_1_G, tmp_1_B);
		sense.set_pixel(x+1, 0, tmp_1_R, tmp_1_G, tmp_1_B);
		sense.set_pixel(x+1, 1, tmp_1_R, tmp_1_G, tmp_1_B);

		sense.set_pixel(x, 3, tmp_2_R, tmp_2_G, tmp_2_B);
		sense.set_pixel(x, 4, tmp_2_R, tmp_2_G, tmp_2_B);
		sense.set_pixel(x+1, 3, tmp_2_R, tmp_2_G, tmp_2_B);
		sense.set_pixel(x+1, 4, tmp_2_R, tmp_2_G, tmp_2_B);

		sense.set_pixel(x, 6, tmp_3_R, tmp_3_G, tmp_3_B);
		sense.set_pixel(x, 7, tmp_3_R, tmp_3_G, tmp_3_B);
		sense.set_pixel(x+1, 6, tmp_3_R, tmp_3_G, tmp_3_B);
		sense.set_pixel(x+1, 7, tmp_3_R, tmp_3_G, tmp_3_B);
		sleep(0.1)
		a = a + 1

def blinkRow(x):
	a=0
	for i in range (8):
		if(i==0):
			tmp_1 = sense.get_pixel(x, i);
			tmp_1_R = tmp_1[0]
			tmp_1_G = tmp_1[1]
			tmp_1_B = tmp_1[2]
		if(i==3):
			tmp_2 = sense.get_pixel(x,i)
			tmp_2_R = tmp_2[0]
			tmp_2_G = tmp_2[1]
			tmp_2_B = tmp_2[2]
		if(i==6):
			tmp_3 = sense.get_pixel(x,i)
			tmp_3_R = tmp_3[0]
			tmp_3_G = tmp_3[1]
			tmp_3_B = tmp_3[2]

	while a<10:
		sense.set_pixel(0, x, 0, 0, 0);
		sense.set_pixel(1, x, 0, 0, 0);
		sense.set_pixel(0, x+1, 0, 0, 0);
		sense.set_pixel(1, x+1, 0, 0, 0);

		sense.set_pixel(3, x, 0, 0, 0);
		sense.set_pixel(4, x, 0, 0, 0);
		sense.set_pixel(3, x+1, 0, 0, 0);
		sense.set_pixel(4, x+1, 0, 0, 0);

		sense.set_pixel(6, x, 0, 0, 0);
		sense.set_pixel(7, x, 0, 0, 0);
		sense.set_pixel(6, x+1, 0, 0, 0);
		sense.set_pixel(7, x+1, 0, 0, 0);
		sleep(0.1)
		sense.set_pixel(0, x, tmp_1_R, tmp_1_G, tmp_1_B);
		sense.set_pixel(1, x, tmp_1_R, tmp_1_G, tmp_1_B);
		sense.set_pixel(0, x+1, tmp_1_R, tmp_1_G, tmp_1_B);
		sense.set_pixel(1, x+1, tmp_1_R, tmp_1_G, tmp_1_B);

		sense.set_pixel(3, x, tmp_2_R, tmp_2_G, tmp_2_B);
		sense.set_pixel(4, x, tmp_2_R, tmp_2_G, tmp_2_B);
		sense.set_pixel(3, x+1, tmp_2_R, tmp_2_G, tmp_2_B);
		sense.set_pixel(4, x+1, tmp_2_R, tmp_2_G, tmp_2_B);

		sense.set_pixel(6, x, tmp_3_R, tmp_3_G, tmp_3_B);
		sense.set_pixel(7, x, tmp_3_R, tmp_3_G, tmp_3_B);
		sense.set_pixel(6, x+1, tmp_3_R, tmp_3_G, tmp_3_B);
		sense.set_pixel(7, x+1, tmp_3_R, tmp_3_G, tmp_3_B);
		sleep(0.1)
		a = a + 1
main()
