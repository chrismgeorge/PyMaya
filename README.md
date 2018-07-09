# PyMaya Documentation

## Creating Shapes

### Cube

```markdown
Cube(centerX, centerY, centerZ, width=1, height=1, depth=1, angleX=0, angleY=0, angleZ=0, fill=rgb(#, #, #))

# create a minimal cube (default color is white if no fill specified)
c = Cube(0, 0, 0)

# move the cube
c.centerX += 10

# rotate the cube
c.angleX += 10
```

### Setting Key Frames
```markdown
shape.setKeyFrame(frame)

# Animation that has a cube start at 0, 0, 0 and move to 0, 0, 10 on frame 10
c = Cube(0, 0, 0)
c.setKeyFrame(0)
c.centerX += 10
c.setKeyFrame(10)
```



```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/chrismgeorge/PyMaya/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
