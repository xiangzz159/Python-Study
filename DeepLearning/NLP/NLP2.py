# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/27 17:02

@desc: https://mp.weixin.qq.com/s?__biz=MjM5MjAwODM4MA==&mid=2650703472&idx=2&sn=3fb9dff5f2e50b46f3e1c8dcd87677be&chksm=bea6f7a389d17eb5b1c72aad83378b7a673a57edec759b4b99f0341fc2aea4675d998a648b44&scene=0#rd

'''

import spacy

# Load the large English NLP model
nlp = spacy.load('en_core_web_lg')


# Replace a token with "REDACTED" if it is a name
def replace_name_with_placeholder(token):
    if token.ent_iob != 0 and token.ent_type_ == 'PERSON':
        return '[REDACTED]'
    else:
        return token.string


# Loop through all the entities in a document and check if they are names
def scrub(text):
    doc = nlp(text)
    for ent in doc.ents:
        ent.merge()
    tokens = map(replace_name_with_placeholder, doc)
    return ''.join(tokens)


s = """
n 1950, Alan Turing published his famous article "Computing Machinery and Intelligence". In 1957, Noam Chomsky’s 
Syntactic Structures revolutionized Linguistics with 'universal grammar', a rule based system of syntactic structures.
"""

print(scrub(s))
