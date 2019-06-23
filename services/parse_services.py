import xml.etree.ElementTree as ET
import glob, os

def parseXML(filename):
    val = {
        'Attribute Handle': 0,
        'End Group Handle': 0,
        'UUID': 0,
        'Service type': '',
        'Characteristics': []
    }
    root = ET.parse(filename).getroot()
    val['UUID'] = root.attrib.get('uuid')
    val['Service type'] = root.attrib.get('name')
    return val

def main():
    for file in glob.glob("*.xml"):
        service = parseXML(file)
        print(service)

if __name__== "__main__":
    main()