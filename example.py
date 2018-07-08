from Cube import Cube
from PyMaya import rgb
import maya.cmds as cmds

screenObjects = cmds.ls("pCube*", "blinn*")
if (len(screenObjects) > 0): cmds.delete(screenObjects)

def getDataFromFile(fileName):
    with open(fileName, 'r') as f:
        data = eval(f.read())
    return data
    
def animateNotes(notes):
    global frame
    for i in song:
        i = int(i)
        
        for pix in range(i*8):
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
            cmds.select(curPix)
            # Animate Pixel
            cmds.currentTime(frame)
            cmds.select(curPix)
            cmds.setKeyframe()
            
            # 3) Move note up and make small
            cmds.currentTime((frame + 20))
            cmds.move(0, 20, 0, r=True)
            cmds.scale(0,0,0)
            cmds.setKeyframe()
        frame += tempo

def makeImage():
    planes = getDataFromFile('/Volumes/Users/cmgeorge/documents/chapPall.txt')

    notes = []
    for row in range(len(planes)):
        curRowNotes = []
        for col in range(len(planes[0])):
            Cube(row*.25, 0, col*.25, width=.25, height=.25, depth=.25,
                       fill=rgb(planes[row][col][0], planes[row][col][1], planes[row][col][2]))
            curRowNotes.append(pix)
        notes.append(curRowNotes)
        
    #animateNotes(notes)
    
makeImage()

