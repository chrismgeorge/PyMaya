from Cube import Cube
from PyMaya import rgb
import maya.cmds as cmds
from random import *

screenObjects = cmds.ls("pCube*", "blinn*")
cmds.callbacks(clearAllCallbacks = True)
if (len(screenObjects) > 0): cmds.delete(screenObjects)

def getDataFromFile(fileName):
    with open(fileName, 'r') as f:
        data = eval(f.read())
    return data
    
def animateNotes():
    curFrame = 50
    tempo = 2.225
    song = getDataFromFile('/Volumes/Users/cmgeorge/documents/pMan.txt')
    normalizer = 4.0
    colorScaler = 255 / (max(song) / normalizer)
    for i in range(len(song)):
        frameDensity = song[i]
        newFill = rgb(255 - frameDensity*colorScaler, 0, frameDensity*colorScaler)
        newC = Cube(i, 0, 0, fill=newFill) 
        newC.setKeyFrame(curFrame - 1)
        newC.setWHD(1, frameDensity, 1)
        newC.setKeyFrame(curFrame + 3)
        curFrame += tempo

animateNotes()


