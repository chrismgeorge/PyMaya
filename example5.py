from PyMaya import rgb
import maya.cmds as cmds
from random import *
from Plane import Plane

screenObjects = cmds.ls("pCube*", "blinn*", "pPlane*")
cmds.callbacks(clearAllCallbacks = True)
if (len(screenObjects) > 0): cmds.delete(screenObjects)

def getDataFromFile(fileName):
    with open(fileName, 'r') as f:
        data = eval(f.read())
    return data
    
def animateNotes():
    curFrame = 50
    tempo = 2.23
    song = getDataFromFile('/Volumes/Users/cmgeorge/documents/yesterday.txt')
    p = Plane(0, 0, 0, width=50, depth=50, sx=len(song[0]), sy=len(song[0][0]))
    for songBlock in song:
        for rowIndex, songRow in enumerate(songBlock):
            for colIndex, ele in enumerate(songRow):
                ele = ele / 100
                p.moveVerticeRelative(rowIndex, colIndex, 0, ele, 0, curFrame)
                p.moveVerticeRelative(rowIndex, colIndex, 0, -ele, 0, curFrame + 1)
        curFrame += tempo
    

animateNotes()


