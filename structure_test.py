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

class RPCell :
    def __init__(self,color,x,y):
        self.color=color

    def display(self):
        for i in range 2:
            for j in range 2:
                sense.set_pixel(x*3+i, y*3+j, self.color)

class RPFace :
    def __init__(self,color,top=None,right=None,bottom=None,left=None):
        self.top=top
        self.right=right
        self.bot=bottom
        self.left=left
        self.cells=[]
        for i in range 3:
            for j in range 3
                self.cells.append(RPCell(color,i,j))
        
    def setSide(self,side,face):
        if side=top :
            self.top=face
        elif side=right :
            self.right=face
        elif side=bot :
            self.bot=face
        elif side=left :
            self.left=face

    def display(self):
        for i in self.cells:
            self.cells[i].display()


class RPCube :
    def __init__(self):
        self.face1=RPFace(r)
        self.face2=RPFace(b,top=self.face1)
        self.face3=RPFace(g,top=self.face1,left=self.face2)
        self.face4=RPFace(y,top=self.face1,left=self.face3)
        self.face5=RPFace(c,top=self.face1,left=self.face4,right=self.face2)
        self.face6=RPFace(m,top=self.face2,right=self.face3,bot=self.face4,left=self.face5)
        self.face1.setSide(top=self.face4)
        self.face1.setSide(right=self.face3)
        self.face1.setSide(bot=self.face2)
        self.face1.setSide(left=self.face5)
        self.face2.setSide(right=self.face3)
        self.face2.setSide(bot=self.face6)
        self.face2.setSide(left=self.face5)
        self.face3.setSide(right=self.face4)
        self.face3.setSide(bot=self.face6)
        self.face4.setSide(bot=self.face6)
        self.face4.setSide(right=self.face5)
        self.face5.setSide(bot=self.face6)

    def display(self):
        self.face1.display();




cube=RPCube()

cube.display()



sense.clear()

        


