class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSerch(nums, target, True)
        right = self.binSerch(nums, target, False)
        return [left, right]
    # 注意寻找目标值和找到目标值后偏置时的区别
    # 寻找目标值时根据目标值大小决定的和中间值的相对位置来调整左右边界
    # 偏置时只是根据偏置方向调整边界
    def binSerch(self, nums, target, leftBias):  # 添加偏置条件
        l, r = 0, len(nums) - 1
        i = -1  # 返回的值，默认为-1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                i = m
                if leftBias:  # 左偏
                    r = m - 1
                else:
                    l = m + 1
        return i
