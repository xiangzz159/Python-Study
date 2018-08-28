#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/28 11:29

@desc: https://mp.weixin.qq.com/s?__biz=MjM5MjAwODM4MA==&mid=2650703472&idx=2&sn=3fb9dff5f2e50b46f3e1c8dcd87677be&chksm=bea6f7a389d17eb5b1c72aad83378b7a673a57edec759b4b99f0341fc2aea4675d998a648b44&scene=0#rd

'''

import spacy
import textacy.extract

nlp = spacy.load('en_core_web_lg')

text = """London is the capital and most populous city of England and  the United Kingdom.  
Standing on the River Thames in the south east of the island of Great Britain, 
London has been a major settlement  for two millennia.  It was founded by the Romans, 
who named it Londinium.
"""

doc = nlp(text)

statements = textacy.extract.semistructured_statements(doc, "London")

print('Here are thr things I know about London:')

for statement in statements:
    subject, verb, fact = statement
    print(f' - {fact}')