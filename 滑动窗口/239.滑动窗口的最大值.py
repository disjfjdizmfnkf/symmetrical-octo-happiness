from collections import deque
from typing import List

# k > 0  nums.length > 0

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        deq = deque()
        for l in range(len(nums)):
            while deq and deq[0] < l - k + 1:  # 移除窗口外的数的索引
                deq.popleft()
            # 实现单调队列, 维护左边的数字比右边大
            while deq and nums[deq[-1]] < nums[l]:
                deq.pop()
            deq.append(l)
            # 窗口形成后, 每次都取最大值
            if l + 1 >= k:
                res.append(nums[deq[0]])
        return res
