from pymel.core import *

class Shape(object):
    def __init__(self, shape, centerX, centerY, centerZ):
        self._shape = shape[0]
        
        self._centerX = centerX
        self._centerY = centerX
        self._centerZ = centerZ
        
    def updateShape(self):
        self._shape.translate.set([self._centerX, self._centerY, self._centerZ])
    
    @property
    def centerZ(self):
        return self._centerZ
    
    @centerZ.setter
    def centerZ(self, value):
        self._centerZ = value
        self.updateShape()
