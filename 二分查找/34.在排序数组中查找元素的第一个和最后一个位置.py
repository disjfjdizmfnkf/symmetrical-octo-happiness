class Solution:
    # 通过二分查找添加偏置条件获取左右边界值
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]

    # 添加偏置参数，在一段相同的数字中获取最左边或最右边的数字
    def binSearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1  # 默认的返回的值
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            # 找到target后根据偏置条件找到边界
            else:
                i = mid
                if leftBias:
                    r = mid - 1
                else:
                    l = mid + 1
        return i