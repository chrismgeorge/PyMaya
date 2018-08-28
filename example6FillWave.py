from Cube import Cube
from Plane import Plane
from PyMaya import rgb
from PyMaya import waveDeformer
import maya.cmds as cmds
from random import *

screenObjects = cmds.ls("pCube*", "pPlane*", "wave1Handle")
cmds.callbacks(clearAllCallbacks = True)
if (len(screenObjects) > 0): cmds.delete(screenObjects)

def getDataFromFile(fileName):
    with open(fileName, 'r') as f:
        data = eval(f.read())
    return data

def animateNotes():
    curFrame = 50
    tempo = 2.227
    song = getDataFromFile('Users/cmgeorge/Documents/hollow.txt')
    normalizer = 4.0
    colorScaler = 255 / (max(song) / 1.0)
    ogColor = rgb(255, 0, 0)
    mapping = Plane(0, 0, 0, width=60, depth=60, sx=50, sy=50, fill=ogColor)
    mapping2 = Plane(-60, 0, 0, width=60, depth=60, sx=50, sy=50, fill=ogColor)
    mapping3 = Plane(0, 0, 60, width=60, depth=60, sx=50, sy=50, fill=ogColor)
    maxNum = max(song)
    for i in range(len(song)):
        if i % 2 != 0:
            curFrame += tempo
            continue
        frameDensity = song[i]
        newFill = rgb(255, 0, frameDensity*colorScaler)
        frameAmplitude = song[i] / (2 * maxNum / 1.0)
        
        # Change color and wave
        mapping.fill = newFill
        mapping.waveDeformer = waveDeformer(amplitude=-frameAmplitude, minRadius=0)
        mapping.setKeyFrame(curFrame)
        mapping2.fill = newFill
        mapping2.waveDeformer = waveDeformer(amplitude=-frameAmplitude, minRadius=0)
        mapping2.setKeyFrame(curFrame)
        mapping3.fill = newFill
        mapping3.waveDeformer = waveDeformer(amplitude=-frameAmplitude, minRadius=0)
        mapping3.setKeyFrame(curFrame)
        
        # Change color and wave
        #mapping.fill = ogColor
        #mapping.waveDeformer = waveDeformer(amplitude=-frameAmplitude, minRadius=1)
        #mapping.setKeyFrame(curFrame + 8)
        
        curFrame += tempo



animateNotes()











