# 假设为理想情况，数组中有目标值等
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:       #结束的时候left + 1 = right，不能等
            mid = (right + left)//2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            elif target == nums[mid]:
                return mid
        return left

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