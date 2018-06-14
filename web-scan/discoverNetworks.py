# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/6/14 14:07

@desc:

'''

import winreg


def val2addr(val):
    addr = ""
    for ch in val:
        addr += ("%02x " % ord(ch))
        addr = addr.strip(" ").replace(" ", ":")[0:17]
    return addr


def printNets():
    net = 'SOFTWARE\Microsoft\Windows NT\CurrentVersion\\NetworkList\Signatures\\Unmanaged'
    print(net)
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, net)
    print('\n[*] Networks You have Joined.')
    for i in range(100):
        try:
            guid = winreg.EnumKey(key, i)
            netKey = winreg.OpenKey(key, str(guid))
            (n, addr, t) = winreg.EnumValue(netKey, 5)
            (n, name, t) = winreg.EnumValue(netKey, 4)
            macAddr = val2addr(addr)
            netName = str(name)
            print('[+] ' + netName + ' ' + macAddr)
            winreg.CloseKey(netKey)
        except:
            break


def main():
    printNets()


if __name__ == "__main__":
    main()
