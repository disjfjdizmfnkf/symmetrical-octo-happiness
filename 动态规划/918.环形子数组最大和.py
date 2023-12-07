class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        curMax = 0
        curMin = 0
        maxSub = nums[0]
        minSub = nums[0]
        for i in nums:
            curMax = max(curMax + i, i)
            maxSub = max(curMax, maxSub)
            curMin = min(curMin + i, i)
            minSub = min(curMin, minSub)
            total += i
        return max(maxSub, total - minSub) if maxSub > 0 else maxSub # 最大值为负数
