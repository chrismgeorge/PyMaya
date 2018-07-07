#from pymel.core import *

class Shape(object):
    def __init__(self, shape, centerX, centerY, centerZ, width, height, depth,
                              angleX=0, angleY=0, angleZ=0):
        self._shape = shape[0]
        
        self._centerX = centerX
        self._centerY = centerX
        self._centerZ = centerZ

        self._angleX = angleX
        self._angleY = angleY
        self._angleZ = angleZ

        self._width = width
        self._height = height
        self._depth = depth
        
    def updateShape(self):
        #self._shape.translate.set([self._centerX, self._centerY, self._centerZ])
        #self._shape.rotate.set([self._angleX, self._angleY, self._angleZ])
        #self._shape.transform.set([self._width, self._height, self._depth])
        pass
    
    # center x, y, z getters and setters
    @property
    def centerX(self):

        return self._centerX
    
    @centerX.setter
    def centerX(self, value):
        self._centerX = value
        self.updateShape()

    @property
    def centerY(self):
        return self._centerY
    
    @centerY.setter
    def centerY(self, value):
        self._centerY = value
        self.updateShape()

    @property
    def centerZ(self):
        return self._centerZ
    
    @centerZ.setter
    def centerZ(self, value):
        self._centerZ = value
        self.updateShape()

    # angle x, y, z getters and setters
    @property
    def angleX(self):
        return self._angleX
    
    @angleX.setter
    def angleX(self, value):
        self._angleX = value
        self.updateShape()

    @property
    def angleY(self):
        return self._angleY
    
    @angleY.setter
    def centerY(self, value):
        self._angleY = value
        self.updateShape()

    @property
    def angleZ(self):
        return self._angleZ
    
    @angleZ.setter
    def angleZ(self, value):
        self._angleZ = value
        self.updateShape()

    # Width, height, depth, getters and setters
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value
        self.updateShape()

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value
        self.updateShape()

    @property
    def depth(self):
        return self._depth
    
    @depth.setter
    def depth(self, value):
        self._depth = value
        self.updateShape()

    
