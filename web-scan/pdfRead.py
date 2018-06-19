# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/6/19 13:38

@desc: 提取PDF元数据

'''

import optparse
import PyPDF2

def printMeta(fileName):
    pdfFile = PyPDF2.PdfFileReader(open(fileName, 'rb'))
    docInfo = pdfFile.getDocumentInfo()
    print('[*] PDF MetaData For: ' + str(fileName))
    for metaItem in docInfo:
        print('[+] ' + metaItem + ':' + docInfo[metaItem])


def main():
    parser = optparse.OptionParser('usage %prog -F <PDF file name>')
    parser.add_option('-F', dest='fileName', type='string', help='specify PDF file name')
    (options, args) = parser.parse_args()
    fileName = options.fileName
    if fileName == None:
        print(parser.usage)
        exit(0)
    else:
        printMeta(fileName)


if __name__ == '__main__':
    main()
