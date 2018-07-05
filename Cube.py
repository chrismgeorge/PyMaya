from PyMaya import *
from pymel.core import *

class Cube(Shape):
    def __init__(self, centerX, centerY, centerZ):
        shape = polyCube()
        super(Cube, self).__init__(shape, centerX, centerY, centerZ)