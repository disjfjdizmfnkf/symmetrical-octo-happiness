# 二分法的精髓似乎就是：
# 1. **判断** 目标(要寻找的值) **在m的左边还是右边**
# 2. 有时(难题)需要借助其他值来判断 这个值也叫 pivot
# 3. 所以我们经常要用分类讨论
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if target > nums[r]:
                if nums[m] > nums[r] and nums[m] < target:
                    l = m + 1
                elif nums[m] == target:
                    return m
                else:
                    r = m - 1
            else:
                if nums[m] > target and nums[m] < nums[r]:
                    r = m - 1
                elif nums[m] == target:
                    return m
                else:
                    l = m + 1
        return -1
