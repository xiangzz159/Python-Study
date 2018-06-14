#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/6/13 15:54

@desc: 在FTP服务器上寻找WEB页面

'''

import ftplib

def returnDefault(ftp):
    try:
        dirList = ftp.nlst()
    except:
        dirList = []
        print('[-] Could not list directory contents.')
        print('[-] Skipping To Next Target.')
        return
    retList = []

    for fileName in dirList:
        fn = fileName.lower()
        if '.php' in fn or '.htm' in fn or '.aps' in fn:
            print('[+] Found default page: ' + fileName)
            retList.append(fileName)
            return retList

host = '192.168.95.179'
username = 'root'
password = 'root'

ftp = ftplib.FTP(host)
ftp.login(username, password)
returnDefault(ftp)