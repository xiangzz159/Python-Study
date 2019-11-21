# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/11/20 16:10

@desc:

'''

import sys, os, re

r = open("/Users/xiangguangye/workspace/Python-Study/data/ltts_slowsql.log.2019-10-23-1", "r+")
fr = r.readlines()
lts = []
results = []
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

w = open("/Users/xiangguangye/workspace/Python-Study/data/onl.log", "w+")
print('*' * 50)
for i in results:
    w.writelines(i)
    # print(i)
w.flush()
w.close()
