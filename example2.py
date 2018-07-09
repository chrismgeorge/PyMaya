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
    tempo = 2.3
    song = getDataFromFile('/Volumes/Users/cmgeorge/documents/csongScale.txt')
    normalizer = 4
    colorScaler = 255 / (max(song) / normalizer)
    for frameDensity in song:
        frameDensity = int(frameDensity / normalizer)
        for pix in range(frameDensity):
            newFill = rgb(255 - frameDensity*colorScaler, 0, frameDensity*colorScaler)
            newC = Cube(randint(-10, 10), 0, randint(-10, 10), width=0, height=0, depth=0, fill=newFill) 
            newC.setKeyFrame(curFrame - 1)
            newC.centerY += 10
            newC.setWHD(1, 1, 1)
            newC.setKeyFrame(curFrame + 5)
            newC.centerY += 10
            newC.centerX += randint(-10, 10)
            newC.centerZ += randint(-10, 10)
            newC.setWHD(0, 0, 0)
            newC.setKeyFrame(curFrame + 10)
        curFrame += tempo

animateNotes()


