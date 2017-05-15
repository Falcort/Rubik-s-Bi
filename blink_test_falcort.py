from sense_hat import SenseHat
from time import sleep
from random import *

sense = SenseHat()
sense.clear()
r = [255,0,0]
g = [0,255,0]
b = [0,0,255]
w = [0,0,0]
p = [255,0,255]
gb = [0,255,255]
rg = [255,255,0]

List = [r, g , b , p, gb, rg]
image = [
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w
]

def main():
	sense.set_pixels(image)
	full()
	init = 10;
	blinkLine(0, init)
	blinkLine(3, init)
	blinkLine(6, init)
	blinkRow(0, init)
	blinkRow(3, init)
	blinkRow(6, init)
	disco()


def disco():
	init = 10
	number = [0, 3, 6]
	times = [1, 2]

	while 1>0:
		int = choice(number)
		nbtimes = choice(times)
		waylist = [blinkLine(int, nbtimes), blinkRow(int, nbtimes)]
		final = choice(waylist)
		full()
def full():
	one = choice(List)
	two = choice(List)
	three = choice(List)
	four = choice(List)
	five = choice(List)
	six = choice(List)
	seven = choice(List)
	eight = choice(List)
	nine = choice(List)

	sense.set_pixel(0,0, one)

	sense.set_pixel(3,0, two)

	sense.set_pixel(6,0, three)

	sense.set_pixel(6,3, four)

	sense.set_pixel(6,6, five)

	sense.set_pixel(3,3, six)

	sense.set_pixel(3,6, seven)

	sense.set_pixel(0, 3, eight)

	sense.set_pixel(0,6, nine)

	init = 1;
	blinkLine(0, init)
	blinkLine(3, init)
	blinkLine(6, init)
	blinkRow(0, init)
	blinkRow(3, init)
	blinkRow(6, init)



def blinkLine(x, number):
	a=0
	for i in range (8):
		if(i==0):
			tmp_1 = sense.get_pixel(x,i);
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

	while a<number:
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

def blinkRow(x, number):
	a=0
	for i in range (8):
		if(i==0):
			tmp_1 = sense.get_pixel(i,x);
			tmp_1_R = tmp_1[0]
			tmp_1_G = tmp_1[1]
			tmp_1_B = tmp_1[2]
		if(i==3):
			tmp_2 = sense.get_pixel(i,x)
			tmp_2_R = tmp_2[0]
			tmp_2_G = tmp_2[1]
			tmp_2_B = tmp_2[2]
		if(i==6):
			tmp_3 = sense.get_pixel(i,x)
			tmp_3_R = tmp_3[0]
			tmp_3_G = tmp_3[1]
			tmp_3_B = tmp_3[2]

	while a<number:
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
