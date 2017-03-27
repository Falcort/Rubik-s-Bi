from sense_hat import SenseHat
from time import sleep
from collections import namedtuple

sense = SenseHat()
sense.clear()

class RPCell :
    def __init__(self,color,x,y):
        self.c=color

class RPColumn :
    def __init__(self,x,c1,c2,c3):
        self.x=x
        self.c1=c1
        self.c2=c2
        self.c3=c3

class RPLine :
    def __init__(self,y,c1,c2,c3):
        self.y=y
        self.c1=c1
        self.c2=c2
        self.c3=c3

class RPFace :
    def __init__(self,top=None,right=None,bottom=None,left=None):
        self.top=top
        self.right=right
        self.bot=bottom
        self.left=left
    def setSide(self,side,face):
        if side=top :
            self.top=face
        elif side=right :
            self.right=face
        elif side=bot :
            self.bot=face
        elif side=left :
            self.left=face


class RPCube :
    def __init__(self):
        self.face1=RPFace()
        self.face2=RPFace(top=self.face1)
        self.face3=RPFace(top=self.face1,left=self.face2)
        self.face4=RPFace(top=self.face1,left=self.face3)
        self.face5=RPFace(top=self.face1,left=self.face4,right=self.face2)
        self.face6=RPFace(top=self.face2,right=self.face3,bot=self.face4,left=self.face5)
        self.face1.setSide(top=self.face4)
        self.face1.setSide(right=self.face3)
        self.face1.setSide(bot=self.face2)
        self.face1.setSide(left=self.face5)
        self.face2.setSide(right=self.face)
        self.face2.setSide(bot)
        self.face2.setSide(left)
        self.face3.setSide(right)
        self.face3.setSide(bot)
        self.face4.setSide(bot)








sense.clear()

        


