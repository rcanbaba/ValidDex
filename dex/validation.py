#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
import io
import platform
import xml.etree.ElementTree as ET
from collections import defaultdict
import random
import string

dv = defaultdict(lambda: 0)
xml_List = []
ce = []
result = {}
empty_dict = dict.fromkeys(['id', "name"])

def runValid(dirname,baseClass):

    a = find_all(dirname,baseClass)
    b = convert_text(dv)
    ch = ''.join(random.choice(string.ascii_letters) for x in range(5))
    na = 'out' + '--' + ch
    c = writeDir(na, b)

def find_all(dirname, baseClass):
    items = os.listdir(dirname)

    for item in items:
        if item[-3:] != "xml":
            continue
        find_one(os.path.join(dirname, item), baseClass)

def convert_text(lst):
    text = ""
    for item in lst:
        text = '{}\n{}'.format(text, item)
    return text

def writeDir(filename, content):
    if platform.system() == 'Windows':
        desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
    else:
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

    xq = desktop + "/" + filename
    print("filename", xq)

    # global result_Label
    try:
        with io.open(xq, 'w') as fp:
            fp.write(content)

    except:
        pass


def find_one(filename, baseClass):
    root = ET.parse(filename).getroot()

    baseClassNames = parse_classes_file(baseClass)
    for obj in root.iter('object'):
        c = obj.find('name').text
        d = root.find("filename").text
        ce.append({"c": c, "d": d})


    global xa
    for k in range(len(ce)):
        xa = False
        for i in range(len(baseClassNames)):
            if baseClassNames[i] == ce[k]["c"]:
                xa = True
                break

        if xa == False:
            c = ce[k]["c"]
            d = ce[k]["d"]
            dv[c + "---" + d] += 1

def read(filename):
    with open(filename, 'r') as f:
        return f.read()


def parse_classes_file(filename):
    content = read(filename).split('\n')
    return [item.strip() for item in content if item != '']


def writeToJSONFile(path, fileName, data):
    filePathNameWExt = '' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)
