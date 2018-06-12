#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/6/11 19:29

@desc: http://www.dayexie.com/detail2217031.html

'''

# coding=UTF-8
import optparse
import nmap

def nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner(nmap_search_path=('nmap', r'E:\Program Files (x86)\Nmap\nmap.exe'))
    results = nmScan.scan(tgtHost, tgtPort)
    if len(results['scan']) > 0:
        state = results['scan'][tgtHost]['tcp'][int(tgtPort)]['state']
        print(" [*] " + tgtHost + " tcp/" + tgtPort + " " + state)
    else:
        print('result scan length is Nonr')
def main():
    parser = optparse.OptionParser('usage %prog –H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target port')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = options.tgtPort
    args.append(tgtPort)
    if (tgtHost == None) | (tgtPort == None):
        print('[-] You must specify a target host and port[s]!')
        exit(0)
    for tgport in args:
        nmapScan(tgtHost, tgport)
if __name__ == '__main__':
    main()
