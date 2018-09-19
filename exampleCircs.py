from Cylinder import Cylinder
from PyMaya import rgb
from PyMaya import squashDeformer
import maya.cmds as cmds
from random import *

screenObjects = cmds.ls("pCylinder*", "pPlane*", "wave1Handle")
cmds.callbacks(clearAllCallbacks = True)
if (len(screenObjects) > 0): cmds.delete(screenObjects)

def getDataFromFile(fileName):
    with open(fileName, 'r') as f:
        data = eval(f.read())
    return data

def animateNotes():
    curFrame = 50
    tempo = 2.25
    song = getDataFromFile('Users/cmgeorge/Documents/isolated_vocals.txt')
    colorScaler = 255 / (max(song) / 1.0)
    
    for i in range(len(song)):

        frameDensity = song[i]
        red = min(frameDensity*colorScaler*2, 255)
        green = max(0, 255 - frameDensity*colorScaler*2)
        curBlock = Cylinder(0, 10, 0, angleX=90, fill=rgb(red, green, 255))
        
        # Set animation to occur within correct frame
        curBlock.height = 0
        curBlock.width = 0
        curBlock.depth = 0
        curBlock.setKeyFrame(curFrame - 1)
        
        # Change color and deformer
        curBlock.height = 1
        curBlock.width = frameDensity / 2
        curBlock.depth = frameDensity / 2
        curBlock.setKeyFrame(curFrame)
        
        # Change color and deformer to og set
        curBlock.height = 0
        curBlock.width = 0
        curBlock.depth = 0
        curBlock.centerY += 200
        curBlock.setKeyFrame(curFrame + 48)
        
        curFrame += tempo




animateNotes()











