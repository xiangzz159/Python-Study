# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/6/19 11:11

@desc: 用户id标记回收站文件

'''

import os
import winreg


def returnDir():
    dirs = ['C:\\Recycler\\', 'C:\\Recycled\\', 'C:\\$Recycle.Bin\\']
    for recycleDir in dirs:
        if os.path.isdir(recycleDir):
            return recycleDir
    return None


def sid2user(sid):
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                             'SOFTWARE\Microsoft\Windows NT\CurrentVersion\\ProfileList\\' + sid)
        value, type = winreg.QueryReflectionKey(key, 'ProfileImagePath')
        user = value.split('\\')[-1]
        return user
    except:
        return sid


def findRecycled(recycleDir):
    dirList = os.listdir(recycleDir)
    for sid in dirList:
        files = os.listdir(recycleDir + sid)
        user = sid2user(sid)
        print('\n[*] Listing Files For User: ' + str(user))
        for file in files:
            print('[+] Found File: ' + str(file))


def main():
    recycleDir = returnDir()
    findRecycled(recycleDir)


if __name__ == '__main__':
    main()
