# PyMaya Documentation

## Creating Shapes

### Cube

```markdown
Cube(centerX, centerY, centerZ, width=1, height=1, depth=1, angleX=0, angleY=0, angleZ=0, 
     fill=rgb(#, #, #))

# create a minimal cube (default color is white if no fill specified)
c = Cube(0, 0, 0)

# move the cube
c.centerX += 10

# rotate the cube
c.angleX += 10
```

### Planes

```markdown

```

### Setting Key Frames
```markdown
shape.setKeyFrame(frame)

# Animation that has a cube start at 0, 0, 0 and move to 10, 0, 0 on frame 10
c = Cube(0, 0, 0)
c.setKeyFrame(0)
c.centerX += 10
c.setKeyFrame(10)
```

### Other shape methods
```markdown
shape.setWHD(newWidth, newHeight, newDepth)
width, height, depth = shape.getWHD()
# Getting/Setting the width, height, and depth of a shape in one line each
c = Cube(0, 0, 0, width=20, depth=10)
cWidth, cHeight, cDepth = c.getWHD()
# cWidth=20, cHeight=1, cDepth=10

c.setWHD(10, 100, 18)
cWidth, cHeight, cDepth = c.getWHD()
# cWidth=10, cHeight=100, cDepth=18
```
