import os
import platform
import requests
import string
import random


def writeDir(path):
    print('selected', path)
    if platform.system() == 'Windows':
        pathDir = os.path.normpath(os.path.expanduser('~/Desktop/'))

    else:
        pathDir = os.path.join(os.path.expanduser('~/Desktop/'))

    ch = ''.join(random.choice(string.ascii_letters) for x in range(5))
    global xq
    xq = pathDir + ch
    print(xq)
    if not os.path.exists(xq):
        os.makedirs(xq)

    exeImgUrlList(path)


def read(filename):
    with open(filename, 'r') as f:
        return f.read()


def parseClass(filename):
    content = read(filename).split('\n')
    return [item.strip() for item in content if item != '']


def exeImgUrlList(path):
    imgList = []
    size = 0

    CLASSES = {name: [name, idx] for idx, name in enumerate(parseClass(path))}

    getImgUrl(CLASSES)


def getImgUrl(ImgArr):
    ss = 0
    ImgArr = list(ImgArr)

    for i in range(len(ImgArr)):
        url = ImgArr[i]

        r = requests.get(url, allow_redirects=False)

        open(xq + '/' + str(i) + '.' + "jpg", 'wb').write(r.content)
        ss += 1

    if ss == len(ImgArr):
        getDetectJson(ImgArr)


def getDetectJson(imgUrl):
    global baseUrl
    baseUrl = '# URL Object Detection api url'

    global headers

    headers = {'Content-type': 'application/json'}

    size = 0

    for i in range(len(imgUrl)):

        param ='#your post method parameters'

        r = requests.post(baseUrl, json=param, headers=headers)

        if r.status_code == 200:
            rValue = r.json()
            jsonToXml(rValue, i)
            size += 1


def jsonToXml(content, indis):
    data = content
    con_anno = xq + '/'
    for i in range(len(data)):

        f = open(con_anno + str(indis) + '.xml', 'w')
        line = "<annotation>" + '\n'
        f.write(line)
        line = '\t\t<folder>' + "folder" + '</folder>' + '\n'
        f.write(line)
        line = '\t\t<filename>' + str(i) + '.jpg' + '</filename>' + '\n'
        f.write(line)
        line = '\t\t<source>\n\t\t<database>Unknown</database>\n\t</source>\n'
        f.write(line)

        (width, height) = 1500, 2000

        line = '\t<size>\n\t\t<width>' + str(width) + '</width>\n\t\t<height>' + str(height) + '</height>\n\t'
        line += '\t<depth>3</depth>\n\t</size>'
        f.write(line)
        line = '\n\t<segmented>Unspecified</segmented>'
        f.write(line)

        for anno in data['results']:
            xmin = int(anno['coor']['left'])
            xmax = int(anno['coor']['right'])
            ymin = int(anno['coor']['top'])
            ymax = int(anno['coor']['bottom'])

            line = '\n\t<object>'
            line += '\n\t\t<name>' + anno['name'] + '</name>\n\t\t<pose>Unspecified</pose>'
            line += '\n\t\t<truncated>Unspecified</truncated>\n\t\t<difficult>0</difficult>'
            line += '\n\t\t<bndbox>\n\t\t\t<xmin>' + str(xmin) + '</xmin>'
            line += '\n\t\t\t<ymin>' + str(ymin) + '</ymin>'
            line += '\n\t\t\t<xmax>' + str(xmax) + '</xmax>'
            line += '\n\t\t\t<ymax>' + str(ymax) + '</ymax>'
            line += '\n\t\t</bndbox>'
            line += '\n\t</object>\n'
            f.write(line)

        line = '</annotation>' + '\n'
        f.write(line)
        f.close()
