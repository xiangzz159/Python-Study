#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'657. Judge Route Circle'

import collections

def judgeCirle(self, moves):
    c = collections.Counter(moves)
    return c['L'] == c['R'] and c['U'] == c['D']
