# 更加模板化的解法
class Solution1:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSerch(nums, target, True)
        right = self.binSerch(nums, target, False)
        return [left, right]

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

class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return[-1,-1]
        def find_left(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m # 右边界在大于等于target的位置上 缩小边界
            return l if nums[l] == target else -1
        def find_right(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2 + 1
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m
            return l if nums[l] == target else -1
        return [find_left(nums,target),find_right(nums,target)]
