#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/7/24 15:12

@desc: https://leetcode-cn.com/problems/top-k-frequent-elements/description/

'''

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        re = []
        new_nums = [[0, 0]]
        nums.sort()
        index = 0
        now_num = nums[0]
        for num in nums:
            if now_num != num:
                now_num = num
                new_nums.append([0, 0])
                index += 1
            new_nums[index][0] += 1
            new_nums[index][1] = num
        new_nums.sort(reverse=True)
        n = None
        for count, num in new_nums:
            if len(re) >= k:
                break
            if n == num:
                continue
            re.append(num)
            n = num
        return re



if __name__ == '__main__':
    s = Solution()
    re = s.topKFrequent([1, 5, 2, 1, 2, 5, 1 ,3 ,6 ,9 ,10], 2)
    print(re)