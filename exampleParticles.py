from PyMaya import rgb
from pymel.core import *
import maya.cmds as cmds
from random import *
from Sphere import Sphere
import math

screenObjects = cmds.ls("pSphere*", "nParticle*", "nucleus*", "blinn*", "pPlane*")
cmds.callbacks(clearAllCallbacks = True)
if (len(screenObjects) > 0): cmds.delete(screenObjects)

def getDataFromFile(fileName):
    with open(fileName, 'r') as f:
        data = eval(f.read())
    return data
    
def animateNotes():
    curFrame = 50
    tempo = 2.5
    
    cmds.polySphere()
    cmds.NEmitFromObject()
    cmds.setAttr("nParticleShape1.lifespanMode", 1)
    cmds.setAttr("emitter1.rate", 1)
    for i in range(36):
        dx = (math.pi * i) / 180 * 100
        dy = (math.pi * i) / 180 * 100
        setCurrentTime(i*24)
        cmds.setAttr("nucleus1.gravityDirectionX", dx)
        cmds.setAttr("nucleus1.gravityDirectionY", dy)
        cmds.select("nucleus1")
        setKeyframe()

    
    

animateNotes()


