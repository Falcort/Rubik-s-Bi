from sense_hat import SenseHat
from time import sleep
from collections import namedtuple



sense = SenseHat()
sense.clear()


r = [255,0,0]
g = [0,255,0]
b = [0,0,255]
w = [0,0,0]
m = [255,0,255]
c = [0,255,255]
y = [255,255,0]
colors=[r,g,b,m,c,y]



class RPCube :
    def __init__(self):
        self.cells=[]
        for face in range (6):
            self.cells.append([])
            for line in range (3):
                self.cells[face].append([])
                for column in range (3):
                    self.cells[face][line].append([])
                    self.cells[face][line][column]=colors[face]

    def display(self,face):
        for line in range (3):
            for column in range (3):
                for i in range (2):
                    for j in range (2):
                        sense.set_pixel(line*3+i, column*3+j, self.cells[face][line][column])
                        
	

cube=RPCube()

while True:
    orientation=sense.get_orientation()
    pitch=orientation['pitch']
    roll=orientation['roll']
    yaw=orientation['yaw']

    if( (pitch>315 or pitch<45) and (roll<45 or roll>315)):
        cube.display(4)
    elif( (pitch>315 or pitch<45) and (roll>45 and roll<135)):
        cube.display(0)
    elif( (pitch>315 or pitch<45) and (roll>135 and roll<225)):
        cube.display(5)
    elif( (pitch>315 or pitch<45) and (roll>225 and roll<315)):
        cube.display(2)
    elif( (pitch>45 and pitch<135)s):
        cube.display(3)
    elif( (pitch>225 and pitch<315)):
        cube.display(1)



        


