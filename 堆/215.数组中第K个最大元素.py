"""It's a pretty common case to have to work on data that is pre-sorted or near pre-sorted, so this
implementation with using the last element as the pivot isn't a good choice. Many people have suggested
picking a random element and switching it for the last element, but for arrays where every element has
 the same value that still leaves the input array sorted and still takes quadratic time. An additional
 improvement is to keep track of the last index < pivot and use that for the left window, instead of p-1
 . This eliminates processing duplicates of the pivot repeatedly. E.g.:"""
from random import random
from typing import List


# quick sort 使用快速排序
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        big, equal, small = [], [], []
        for n in nums:
            if n > pivot:
                big.append(n)
            elif n < pivot:
                small.append(n)
            else:
                equal.append(n)
        if k <= len(big): # 在big中
            return self.findKthLargest(big, k)  # 如果这里不使用return，那么结果无法被初始函数返回
        elif k > len(big) + len(equal): # 超过big和equal, k 越大，值越小，从大到小跳过越多
            return self.findKthLargest(small, k - len(big) - len(equal))
        else:
            return pivot