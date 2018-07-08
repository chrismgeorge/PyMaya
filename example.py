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
    
def animateNotes(notes):
    curFrame = 50
    tempo = 2.25
    song = planes = getDataFromFile('/Volumes/Users/cmgeorge/documents/psongIntensity.txt')
    for i in song:
        i = int(i)
        for pix in range(i):
            t = True
            while(t):
                randRow = randint(0, len(notes)-1)
                if (len(notes[randRow]) == 0):
                    continue
                else:
                    t = False
                    randCol = randint(0, len(notes[randRow])-1)

            curPix = notes[randRow][randCol]
            notes[randRow].remove(curPix)
            
            curPix.setKeyFrame(curFrame - 1)
            curPix.centerY += 20
            curPix.width = 0
            curPix.height = 0 
            curPix.depth = 0
            curPix.setKeyFrame(curFrame + 20)

        curFrame += tempo

def makeImage():
    planes = getDataFromFile('/Volumes/Users/cmgeorge/documents/chapPall.txt')

    notes = []
    for row in range(len(planes)):
        curRowNotes = []
        for col in range(len(planes[0])):
            pix = Cube(row*.25, 0, col*.25, width=.25, height=.25, depth=.25,
                       fill=rgb(planes[row][col][0], planes[row][col][1], planes[row][col][2]))
            curRowNotes.append(pix)
        notes.append(curRowNotes)
        
    animateNotes(notes)
    
makeImage()

