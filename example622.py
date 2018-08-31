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
    tempo = 2.23
    song = getDataFromFile('Users/cmgeorge/Documents/haze.txt')
    normalizer = 4.0
    colorScaler = 255 / (max(song) / 1.0)
    blocks = []
    ogColor = rgb(0, 255, 255)
    for i in range(60):
        newC = Cube(i*2, 0, 0)
        blocks.append(newC)
    OldMax = max(song)
    OldMin = min(song)
    NewMax = 20
    NewMin = -10
    for i in range(len(song)):
        curBlock = blocks[i%60]
        frameDensity = song[i]
        newFill = rgb(frameDensity*colorScaler, 255 - frameDensity*colorScaler, 255)
        
        OldRange = (OldMax - OldMin)
        NewRange = (NewMax - NewMin)
        NewValue = (((frameDensity - OldMin) * NewRange) / (OldRange * 1.0)) + NewMin
        
        # Set animation to occur within correct frame
        curBlock.fill = ogColor
        curBlock.height = 1
        curBlock.setKeyFrame(curFrame - 1)
        
        # Change color and deformer
        curBlock.fill = newFill
        curBlock.height = frameDensity
        curBlock.setKeyFrame(curFrame)
        
        # Change color and deformer to og set
        curBlock.fill = ogColor
        curBlock.height = 1
        curBlock.setKeyFrame(curFrame + 16)
        
        curFrame += tempo



animateNotes()











