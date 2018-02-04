#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'760 FindAnagram Mappings'
def anagramMappings(self, A, B):
    d = {}
    for i, b in enumerate(B):
        if b not in d:
            d[b] = []
        d[b].append(i)
    return [d[a].pop() for a in A]