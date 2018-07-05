from pymel.core import *

# Remove All Things from screen
things = cmds.ls("mySphere*")
cmds.callbacks(clearAllCallbacks = True)
if (len(things) > 0):
    cmds.delete(things)

tempo = 3
frame = 50

def getDataFromFile(fileName):
    with open(fileName, 'r') as f:
        data = eval(f.read())
    return data

def setColor(thisObject, thisColor):
    newBlin = cmds.shadingNode('blinn', asShader=True)
    sg = cmds.sets(str(thisObject[0]), renderable=True, 
                   noSurfaceShader=True, empty=True, 
                   name=str(newBlin)+"SG")
    cmds.connectAttr(str(newBlin)+".outColor", str(sg)+".surfaceShader")
    cmds.setAttr(str(newBlin)+".color", 
                 thisColor[0], thisColor[1], thisColor[2], 
                 type='double3')
    cmds.sets(str(thisObject[0]), forceElement=str(sg))   

def makeImage():
    planes = getDataFromFile('/Volumes/Users/cmgeorge/documents/i.txt')
    notes = []
    for row in range(len(planes)):
        curRowNotes = []
        for col in range(len(planes[0])):
            n = polyPlane(name='plan*')
            n[0].translate.set([row*.25, 0, col*.25])
            setColor(n, planes[row][col])
            curRowNotes.append(n)
        notes.append(curRowNotes)
    animateNotes(notes)
    
makeImage()