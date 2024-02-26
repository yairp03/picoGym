import xml.etree.ElementTree as ET

tree = ET.parse("drawing.flag.svg")
root = tree.getroot()
text_component = root[3][3]
texts = [str(component.text) for component in text_component]
print("Flag:", "".join("".join(texts).split()))
