from PyMaya import rgb
from pymel.core import *
import maya.cmds as cmds
from Cube import Cube
from random import *
import math

screenObjects = cmds.ls("pCube*", "nParticle*", "nucleus*", "blinn*")
cmds.callbacks(clearAllCallbacks = True)
if (len(screenObjects) > 0): cmds.delete(screenObjects)

def getDataFromFile(fileName):
    with open(fileName, 'r') as f:
        data = eval(f.read())
    return data

def animateNotes():
    curFrame = 50
    tempo = 2.225
    song = getDataFromFile('/Volumes/Users/cmgeorge/documents/data.txt')
    normalizer = 1.0
    colorScaler = 255 / (max(song) / normalizer)
    dx = 0
    dy = 4
    for i in range(len(song)):
        frameDensity = song[i]
        newFill = rgb(255 - frameDensity*colorScaler, 0, frameDensity*colorScaler)
        cube = Cube(i, 0, 0, fill=newFill)
        cube.setKeyFrame(curFrame)
        cube.setWHD(1, frameDensity, 1)
        cube.setKeyFrame(curFrame + 3)
        
        shape = cube.myShape
        cmds.select(shape)
        cmds.NEmitFromObject()
        setCurrentTime(curFrame)
        cmds.setAttr("nParticleShape"+str(i+1)+".lifespanMode", 1)
        cmds.setAttr("nParticleShape"+str(i+1)+".lifespan", 2)
        cmds.setAttr("nParticleShape"+str(i+1)+".particleRenderType", 8)
        cmds.setAttr("emitter"+str(i+1)+".speed", 7)
        cmds.setAttr("emitter"+str(i+1)+".speedRandom", 4)
        cmds.setAttr("emitter"+str(i+1)+".rate", 0)
        cmds.setAttr("nucleus1.gravityDirectionX", dx)
        cmds.setAttr("nucleus1.gravityDirectionY", dy)
        setKeyframe()
        setCurrentTime(curFrame + 1)
        cmds.setAttr("emitter"+str(i+1)+".rate", 8)
        setKeyframe()
        setCurrentTime(curFrame + 20)
        cmds.setAttr("emitter"+str(i+1)+".rate", 0)
        
        setKeyframe()
        
        curFrame += tempo
        
        # Testing
        if (i == 100):
            break



animateNotes()


