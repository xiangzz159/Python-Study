#！/usr/bin/env python
# _*_ coding:utf-8 _*_

import re

'500. Keyboard Row'


def findWords(self, words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    return filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words)