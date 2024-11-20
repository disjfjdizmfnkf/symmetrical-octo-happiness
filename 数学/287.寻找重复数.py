
# 暴力 n(log(n) + 1) 擦边过的
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        hold = nums[0]
        for i in range(1, len(nums)):
            if hold == nums[i]:
                return hold
            hold = nums[i]
