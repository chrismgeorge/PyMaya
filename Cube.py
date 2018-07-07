from PyMaya import *
#from pymel.core import *

class Cube(Shape):
    def __init__(self, centerX, centerY, centerZ, width=1, height=1, depth=1,
                            angleX=0, angleY=0, angleZ=0):
        #shape = polyCube()
        shape = [1,1]
        super(Cube, self).__init__(shape, centerX, centerY, centerZ, width, 
                                    height, depth, angleX, angleY, angleZ)


a = Cube(10, 10, 10)
a.centerX = 5
print(a.centerX)
