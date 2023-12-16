
# 二分查找 少判断很多边界情况
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            m = l + (r - l) // 2
            if nums[m] < nums[m + 1]:
                l = m
            else:
                r = m

        if nums[l] > nums[r]:
            return l
        return r
