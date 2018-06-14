#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/6/13 9:41

@desc: FTP扫描器

'''
import ftplib

def annonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'me@you.com')
        print('\n[*] ' + str(hostname) + ' FTP Anonymous Logon Successed!')
        ftp.quit()
        return True
    except Exception as e:
        print('\n[-] ' + str(hostname) + ' FTP Anonymous Logon Failed!')
        return False

host = '192.168.95.1'
annonLogin(host)