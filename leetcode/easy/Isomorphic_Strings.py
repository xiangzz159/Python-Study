#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/6/14 17:21

@desc: https://leetcode-cn.com/problems/isomorphic-strings/description/

'''

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_dt = dict()
        for char_s, char_t in zip(s, t):
            if char_s not in char_dt:
                if char_t not in char_dt.values():
                    char_dt[char_s] = char_t
                else:
                    return False
            else:
                if char_dt[char_s] == char_t:
                    pass
                else:
                    return False
        return True


if __name__ == '__main__':
    # t1 = time.time()
    s = Solution()
    str = s.isIsomorphic('ab', 'aa')
    print(str)
    # print(time.time() - t1)