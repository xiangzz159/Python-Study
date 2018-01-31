#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/1/29 11:11

@desc:

'''
def lines(file):
    """
    生成器，在文本最后加一空行
    strip() 函数可以去除一个字符串前后的空格以及换行符，如果在strip()函数添加不同的参数，如strip("me")，则可以去除字符串前后的"me"字符。
    yield()会返回一个生成器(generator)。如果对generator以及对 yiels 语句不太熟悉，建议先阅读yield解释。
    """
    for line in file: yield line
    yield '\n'

def blocks(file):
    """
    生成器，生成单独的文本块
    """
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []

