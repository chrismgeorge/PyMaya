from PyMaya import *
import maya.cmds as cmds
from pymel.core import *

class Cube(Shape):
    def __init__(self, centerX, centerY, centerZ, width=1, height=1, depth=1,
                            angleX=0, angleY=0, angleZ=0, fill=rgb(255, 255, 255)):
        shape = polyCube()
        super(Cube, self).__init__(shape, centerX, centerY, centerZ, width=width, 
                                    height=height, depth=depth, angleX=angleX, 
                                    angleY=angleY, angleZ=angleZ, fill=fill)
