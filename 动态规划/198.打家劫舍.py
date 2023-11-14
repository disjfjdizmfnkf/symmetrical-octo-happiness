
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

        # [rub1, rub2, n, ...]
        for n in nums:
            temp = max(rub1 + n, rub2)
            rub1 = rub2
            rub2 = temp
        return rub2