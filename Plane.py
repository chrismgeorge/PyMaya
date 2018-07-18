from PyMaya import *
import maya.cmds as cmds
from pymel.core import *

class Plane(Shape):
    def __init__(self, centerX, centerY, centerZ, width=1, height=1, depth=1,
                            angleX=0, angleY=0, angleZ=0, fill=rgb(255, 255, 255), 
                            sx=10, sy=10):
        shape = polyPlane(sx=sx, sy=sy)
        self._sx = sx
        self._sy = sy
        self._xVertices = sx + 1
        self._yVerticies = sy + 1
        
        super(Plane, self).__init__(shape, centerX, centerY, centerZ, width=width, 
                                    height=height, depth=depth, angleX=angleX, 
                                    angleY=angleY, angleZ=angleZ, fill=fill)
    # sx means rows
    def moveVerticeAbsolute(self, row, col, x, y, z, frame):
        setCurrentTime(frame)
        vert = (row * self._xVertices) + col
        select(self._shape.vtx[vert])
        cmds.move(x, y, z, a=True)
        setKeyframe()
    
    def moveVerticeRelative(self, row, col, x, y, z, frame):
        setCurrentTime(frame)
        vert = (row * self._xVertices) + col
        select(self._shape.vtx[vert])
        cmds.move(x, y, z, r=True)
        setKeyframe()
        
    def getVertexXYZ(self, row, col):
        vert = (row * self._xVertices) + col
        #select(self._shape.vtx[vert])
        x = getAttr(str(self._shape)+ ".vtx[" + str(vert) + "].translateX")
        y = getAttr(str(self._shape)+ ".vtx[" + str(vert) + "].translateY")
        z = getAttr(str(self._shape)+ ".vtx[" + str(vert) + "].translateZ")
        return [x, y, z]
    
    def setVertexKeyFrame(self, row, col, frame):
        vert = (row * self._xVertices) + col
        select(self._shape.vtx[vert])
        
