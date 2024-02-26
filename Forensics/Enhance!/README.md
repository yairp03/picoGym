# Enhance!

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Forensics  
**Points:** 100

# Challenge

## Description

Download this image file and find the flag.

- [Download image file](./drawing.flag.svg)

## Source

[drawing.flag.svg](./drawing.flag.svg) (Svg Image)

# Solution

Looking at the SVG with a text editor, we can see that the flag's letters are scattered around different `tspan` elements. We can use python's xml parser `xml.etree.ElementTree` to create a [script](./solution.py) that extract the full flag out of the SVG file:

```py
import xml.etree.ElementTree as ET

tree = ET.parse("drawing.flag.svg")
root = tree.getroot()
text_component = root[3][3]
texts = [str(component.text) for component in text_component]
print("Flag:", "".join("".join(texts).split()))
```

**The Flag:** `picoCTF{3nh4nc3d_aab729dd}`
