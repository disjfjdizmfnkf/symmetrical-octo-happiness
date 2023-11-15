
# 用递归理解动态规划
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums, p):
            if p >= len(nums):
                return 0
            if p == len(nums) - 1:
                return nums[p]
            return max(nums[p] + helper(nums, p + 2) , nums[p + 1] + helper(nums, p + 3))
        return helper(nums, 0)
"""


# 动态规划
class Solution:
    def rob(self, nums: List[int]) -> int:
        rub1, rub2 = 0, 0

        # [rub1, rub2, n, n+1, ...]
        for n in nums:
            temp = max(rub1 + n, rub2)  # temp 为可偷到的最大金额 rub1 + n 为偷当前房子，rub2 为不偷当前房子 只有这两种情况
            rub1 = rub2
            rub2 = temp
        return rub2