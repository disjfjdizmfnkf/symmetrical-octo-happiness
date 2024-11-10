# 假设为理想情况，数组中有目标值等
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # 注意最后一个的下标减一

        while left <= right:  # 不超过就是有效
            mid = (left + right) // 2  # 注意要整除
            if target > nums[mid]:
                left = mid + 1
            if target < nums[mid]:
                right = mid - 1
            if target == nums[mid]:
                return mid
        return left  # 为什么总是下界指针？ 因为最后一次循环的时候，left = right + 1

########################################################################################
###                                    注意这个错误                                   ###
########################################################################################

#如果把<=换成<,循环结束的条件是left = right
#那么最后一步是left向右移动了还是right向左移动了？
#所以无法准确求出要插入的位置吗？

class errorSolution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:              
            mid = (right + left)//2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            elif target == nums[mid]:
                return mid
        return left + 1