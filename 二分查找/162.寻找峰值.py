
class Solution1:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # 峰值在比nums[m]大的一侧
        while l <= r:
            m = l + (r - l) // 2
            if m > 0 and nums[m] < nums[m - 1]: # m = 0 时会越界
                r = m - 1
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]: # m = len(nums) - 1 时会越界
                l = m + 1
            else:
                return m

# 二分查找 少判断很多边界情况
class Solution2:
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
