# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/11/21 09:43

@desc:

'''


import os, re

path = r'/Users/xiangguangye/Downloads/19server/bat/slowsql'
filenames = os.listdir(path)

lts = []
results = []
for filename in filenames:
    if 'ltts_slowsql' not in filename:
        continue
    fullpath = path + '/' + filename
    print(fullpath)
    r = open(fullpath, "r+")
    fr = r.readlines()
    for i in fr:
        try:
            ss = i.split('SQL')
            if len(ss) != 2:
                continue
            res_t = r'[[](\d+)[]]'
            m_t = re.findall(res_t, ss[0])
            if int(m_t[-2]) > 400:
                ns = ss[1].strip()
                nss = ns.split(']')
                if nss[0] not in lts:
                    lts.append(nss[0])
                    results.append(i)
        except BaseException as e:
            print(i)
    r.close()

w = open("/Users/xiangguangye/workspace/Python-Study/data/bat.log", "w+")
print('*' * 50)
for i in results:
    w.writelines(i)
    # print(i)
w.flush()
w.close()

