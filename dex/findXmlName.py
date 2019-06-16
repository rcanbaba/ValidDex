import os
import xml.etree.ElementTree as ET


gg =  []


def findAll(dirname, findName):
    items = os.listdir(dirname)

    for item in items:
        if item[-3:] != 'xml':
            continue
        find_one(os.path.join(dirname, item), findName)


def find_one(filename, findName):
    root = ET.parse(filename).getroot()

    for obj in root.iter('object'):
        cc = obj.find('name').text
        dd = root.find('filename').text
        if findName == cc:
            gg.append(dd)
            print("name", gg)
            print("filename", dd)
