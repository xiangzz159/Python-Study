#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/28 13:31

@desc: https://mp.weixin.qq.com/s?__biz=MjM5MjAwODM4MA==&mid=2650703472&idx=2&sn=3fb9dff5f2e50b46f3e1c8dcd87677be&chksm=bea6f7a389d17eb5b1c72aad83378b7a673a57edec759b4b99f0341fc2aea4675d998a648b44&scene=0#rd

'''

import spacy
import textacy.extract

nlp = spacy.load('en_core_web_lg')
text = """Lodon is [.. shortened for space ..]"""

doc = nlp(text)

noun_chunks = textacy.extract.noun_chunks(doc, min_freq=3)

noun_chunks = map(str, noun_chunks)
noun_chunks = map(str.lower, noun_chunks)

for noun_chunk in set(noun_chunks):
    if len(noun_chunk.split(' ')) > 1:
        print(noun_chunk)