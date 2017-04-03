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

"""class RPCell :
    def __init__(self,color,x,y,z):
        self.color=color
	self.x=x
	self.y=y
	self.z=z

    def display(self):
        for i in range (2):
            for j in range (2):
                sense.set_pixel(self.x*3+i, self.y*3+j, self.color)"""
                
"""class RPFace :
    def __init__(self,color,top=None,right=None,bot=None,left=None):
        self.top=top
        self.right=right
        self.bot=bot
        self.left=left
        self.cells=[]
        for i in range(3):
            for j in range(3):
                self.cells.append(RPCell(color,i,j))

    def display(self):
        for i in range(len(self.cells)):
            self.cells[i].display()"""


class RPCube :
    current_face=0
    def __init__(self):
        """self.cells=[]
        for ix in range (2):
            for iy in range (2):
                for iz in range (2):
                    self.cells.append(RPCell(colors[color_cpt%6],ix,iy,iz))
                    color_cpt+=1"""
        self.cells=[]
        for face in range (6):
            self.cells.append([])
            for line in range (3):
                self.cells[face].append([])
                for column in range (3):
                    self.cells[face][line].append([])
                    self.cells[face][line][column]=colors[face]

    def display(self):
        for line in range (3):
            for column in range (3):
                for i in range (2):
                    for j in range (2):
                        sense.set_pixel(line*3+i, column*3+j, self.cells[self.current_face][line][column])
	


cube=RPCube()

cube.display()



        


