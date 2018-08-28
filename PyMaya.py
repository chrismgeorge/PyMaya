from pymel.core import *

class rgb(object):
    def __init__(self, r, g, b):
        self.red = r
        self.green= g
        self.blue = b
    
    def __str__(self):
        return "rgb(%s, %s, %s)" %(str(self.red), str(self.green), str(self.blue))

class waveDeformer(object):
    def __init__(self, amplitude=0.0, wavelength=1.0, offset=0.0, dropoff=0.0, minRadius=0.0,
                 maxRadius=1.0):
        self.amplitude = amplitude
        self.wavelength  = wavelength
        self.offset = offset
        self.dropoff = dropoff
        self.minRadius = minRadius
        self.maxRadius = maxRadius
    
    def __str__(self):
        return "waveDeformer(%s, %s, %s, %s, %s, %s)" %(str(self.amplitude),
                                                        str(self.wavelength),
                                                        str(self.offset),
                                                        str(self.dropoff),
                                                        str(self.minRadius),
                                                        str(self.maxRadius))


WHITE = rgb(255, 255, 255)

class Shape(object):
    def __init__(self, shape, centerX, centerY, centerZ, width, height, depth,
                 angleX=0, angleY=0, angleZ=0, fill=WHITE,
                 waveDeformer=None):
        self._object = shape
        self._shape = shape[0]
        
        self._centerX = centerX
        self._centerY = centerY
        self._centerZ = centerZ
        
        self._angleX = angleX
        self._angleY = angleY
        self._angleZ = angleZ
        
        self._width = width
        self._height = height
        self._depth = depth
        
        self._fill = fill
        self._blinn = None
        self._waveDeformer = waveDeformer
        self._wave = None
        if (self._waveDeformer != None):
            self.setWaveDeformer()
        
        self.setColor()
        
        self._keyedFrames = []
        self.updateShape()
    
    @property
    def waveDeformer(self):
        return self._waveDeformer
    
    def waveDeformerSetAttributes(self):
        cmds.setAttr(str(self._wave[0])+".minRadius", self._waveDeformer.minRadius)
        cmds.setAttr(str(self._wave[0])+".maxRadius", self._waveDeformer.maxRadius)
        cmds.setAttr(str(self._wave[0])+".amplitude", self._waveDeformer.amplitude)
        cmds.setAttr(str(self._wave[0])+".wavelength", self._waveDeformer.wavelength)
        cmds.setAttr(str(self._wave[0])+".dropoff", self._waveDeformer.dropoff)
        cmds.setAttr(str(self._wave[0])+".offset", self._waveDeformer.offset)
    
    @waveDeformer.setter
    def waveDeformer(self, value):
        self._waveDeformer = value
        if self._wave == None:
            self.setWaveDeformer()
        
        self.waveDeformerSetAttributes()
    
    def setWaveDeformer(self):
        select(self._shape)
        self._wave = nonLinear(type='wave')
        self.waveDeformerSetAttributes()
    
    @property
    def keyedFrames(self):
        return self._keyedFrames
    
    def setKeyFrame(self, frame):
        self._keyedFrames.append(frame)
        setCurrentTime(frame)
        self.updateShape()
        setKeyframe()
        cmds.setAttr(str(self._blinn)+".color", self._fill.red / 255.0, self._fill.green / 255.0, self._fill.blue / 255.0,
                     type='double3')
        setKeyframe(str(self._blinn)+".color")
        if (self._waveDeformer != None):
            self.waveDeformerSetAttributes()
            setKeyframe(self._wave[0])

    @property
    def fill(self):
        return self._fill
    
    @fill.setter
    def fill(self, value):
        self._fill = value
        cmds.setAttr(str(self._blinn)+".color", self._fill.red / 255.0,
                     self._fill.green / 255.0, self._fill.blue / 255.0,
                     type='double3')
    
    # Only called once when object is created to create the blinn for the object
    def setColor(self):
        self._blinn = cmds.shadingNode('blinn', asShader=True)
        sg = cmds.sets(str(self._shape), renderable=True, noSurfaceShader=True,
                       empty=True, name=str(self._blinn)+"SG")
        cmds.connectAttr(str(self._blinn)+".outColor", str(sg)+".surfaceShader")
        cmds.setAttr(str(self._blinn)+".color", self._fill.red / 255.0,
                    self._fill.green / 255.0, self._fill.blue / 255.0,
                    type='double3')
        cmds.sets(str(self._shape), forceElement=str(sg))

def updateShape(self):
    select(self._shape)
    # set its movement, rotation, scale, and color
    self._shape.translate.set([self._centerX, self._centerY, self._centerZ])
    rotate(self._angleX, self._angleY, self._angleZ)
    scale(self._depth, self._width, self._height, absolute=True)
    
    
    # custom methods for accessing width, height, and depth all at once
    def getWHD(self):
        return self._width, self._height, self._depth
    
    def setWHD(self, newWidth, newHeight, newDepth):
        self._width = newWidth
        self._height = newHeight
        self._depth = newDepth
        self.updateShape()
    
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
    def angleY(self, value):
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


