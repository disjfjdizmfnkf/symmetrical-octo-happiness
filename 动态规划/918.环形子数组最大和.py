class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSub, minSub = nums[0], nums[0] # 初始的最值要么是计算机中的最值，**要么是变量范围内的任意值**
        curMax, curMin = 0, 0
        total = 0

        for i in nums:
            curMax = max(curMax + i, i)
            maxSub = max(curMax, maxSub)
            curMin = min(curMin + i, i)
            minSub = min(curMin, minSub)
            total += i
        return max(maxSub, total - minSub) if maxSub > 0 else maxSub # 最大值为负数
        # maxSub 和 total - minSub 是两种情况
        # 如果maxSub < 0 说明数组中的元素都是负数