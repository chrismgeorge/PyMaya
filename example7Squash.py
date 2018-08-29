from Cube import Cube
from PyMaya import rgb
from PyMaya import squashDeformer
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
    song = getDataFromFile('Users/cmgeorge/Documents/crush.txt')
    normalizer = 4.0
    colorScaler = 255 / (max(song) / 1.0)
    blocks = []
    ogColor = rgb(255, 255, 255)
    for i in range(8):
        newC = Cube(i*2, 0, 0)
        blocks.append(newC)
    maxNum = max(song)
    for i in range(len(song)):
        curBlock = blocks[i%8]
        frameDensity = song[i]
        newFill = rgb(255 - frameDensity*colorScaler, 255 - frameDensity*colorScaler, 255)
        OldRange = (OldMax - OldMin)
        NewRange = (NewMax - NewMin)
        NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
        
        # Change color and deformer
        curBlock.fill = newFill
        curBlock.squashDeformer = squashDeformer(lowBound=-10, highBound=1, factor=10,
                                                 expand=1, maxExpandPos=.01)
                                                 curBlock.setKeyFrame(curFrame)
                                                 
        # Change color and deformer to og set
        curBlock.fill = ogColor
        curBlock.squashDeformer = squashDeformer(lowBound=-10, highBound=1, factor=-10,
                                              expand=1, maxExpandPos=.01)
        curBlock.setKeyFrame(curFrame + 16)
     
        curFrame += tempo
        if i == 100:
            break



animateNotes()











