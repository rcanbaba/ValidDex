import os
import xml.etree.ElementTree as ET
from collections import defaultdict
from collections import Counter
import json

import platform
import csv


aa = defaultdict(lambda: 0)
gg = []
global _path
pa = ""


def find_One(filename):
    root = ET.parse(filename).getroot()
    for obj in root.iter('object'):
        c = obj.find('name').text
        gg.append(c)
        aa[c] += 1
    count_aa = dict(Counter(gg))

    js_dum = json.dumps(count_aa, ensure_ascii=False, sort_keys=True, indent=4)
    if platform.system() == 'Windows':
        pathDir = os.path.normpath(os.path.expanduser('~/Desktop/'))

    else:
        pathDir = os.path.join(os.path.expanduser('~/Desktop/'))

    ch = pathDir + 'output.csv'
    w = csv.writer(open(ch, 'w'))
    for key, val in count_aa.items():
        w.writerow([key, val])

    # write("gg", json.dumps(gg, ensure_ascii=False, sort_keys=True, indent=4))
    write("prodCount", js_dum)

def convert_text(lst):
    text = ""
    for item in lst:
        text = '{}\n{}.format(text,item)'


def main(dirname):
    items = os.listdir(dirname)

    for item in items:
        if item[-3:] != 'xml':
            continue

        find_One(os.path.join(dirname, item))


def read(filename):
    with open(filename, 'r') as f:
        return f.read()


def parse_classes(filename):
    content = read(filename).split('\n')

    return [item.strip() for item in content if item != ""]


def write(filename, content):
    with open(filename, 'w') as fb:
        fb.write(content)
