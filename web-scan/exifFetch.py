# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/6/20 11:27

@desc: 图片中Exif元数据

'''

import optparse
from bs4 import BeautifulSoup
from os.path import basename
from urllib.parse import urlsplit
from urllib.request import urlopen
from PIL import Image
from PIL.ExifTags import TAGS


def findImages(url):
    print('[+] Finding images on ' + url)
    urlContent = urlopen(url).read()
    soup = BeautifulSoup(urlContent)
    imgTags = soup.findAll('img')
    return imgTags


def downloadImage(imgTag):
    try:
        print('[+] Dowloading image...')
        imgSrc = imgTag['src']
        imgContent = urlopen(imgSrc).read()
        imgFileName = basename(urlsplit(imgSrc)[2])
        imgFile = open(imgFileName, 'wb')
        imgFile.write(imgContent)
        imgFile.close()
        return imgFileName
    except:
        return ''


def testForExif(imgFileName):
    try:
        exifData = []
        imgFile = Image.open(imgFileName)
        info = imgFile._getexif()
        if info:
            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)
                exifData[decoded] = value
        exifGPS = exifData['GPSInfo']
        if exifGPS:
            print('[*] ' + imgFileName + ' contains GPS MetaData')
    except:
        pass


def main():
    parse = optparse.OptionParser('usage%prog -u <target url>')
    parse.add_option('-u', dest='url', type='string', help='specify urladdress')
    options, args = parse.parse_args()
    url = options.url
    if url == None:
        print(parse.usage)
        exit(0)
    else:
        imgTags = findImages(url)
        for imgTag in imgTags:
            imgFileName = downloadImage(imgTag)
            testForExif(imgFileName)


if __name__ == '__main__':
    main()
