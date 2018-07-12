from Cube import Cube
from PyMaya import rgb
import maya.cmds as cmds
from random import *
import math

screenObjects = cmds.ls("pCube*", "blinn*")
cmds.callbacks(clearAllCallbacks = True)
if (len(screenObjects) > 0): cmds.delete(screenObjects)

def getDataFromFile(fileName):
    with open(fileName, 'r') as f:
        data = eval(f.read())
    return data
    
def animateNotes():
    depthMap = getDataFromFile('/Volumes/Users/cmgeorge/documents/depthData.txt')
    imageData = getDataFromFile('/Volumes/Users/cmgeorge/documents/garage.txt')
    imageRows = len(imageData)
    imageCols = len(imageData[0])
    depthRows = len(depthMap)
    depthCols = len(depthMap[0])
    rowScaling = depthRows / float(imageRows)
    colScaling = depthCols / float(imageCols)
    top = imageRows * .25
    for r in range(imageRows):
        for c in range(imageCols):
            pix = imageData[r][c]
            col = rgb(pix[0], pix[1], pix[2])
            depthRow = int(math.floor(r * rowScaling))
            depthCol = int(math.floor(c * colScaling))
            z = float(depthMap[depthRow][depthCol])
            Cube(c * .25, top - (r * .25), z, width=.25, height=.25, depth=.25, fill=col)

animateNotes()
