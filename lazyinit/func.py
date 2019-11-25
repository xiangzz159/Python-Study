# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/11/25 13:47

@desc:

'''


def lazy_property(func):
    attr_name = "_lazy_" + func.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, func(self))
        return getattr(self, attr_name)

    return _lazy_property


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @lazy_property
    def area(self):
        print('evalute')
        return 3.14 * self.radius ** 2


c = Circle(4)
print(c.area)
print(c.area)
