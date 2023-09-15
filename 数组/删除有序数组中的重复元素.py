
#     双指针
# class Solution1:       
#     def removeDuplicates(self, nums: List[int]) -> int:
#         slow, fast = 0, 1
#         while(fast < len(nums)):
#             if nums[fast] != nums[slow]:
#                 slow = slow + 1
#                 nums[slow] = nums[fast]
#             fast = fast + 1
#         return slow + 1


"""
    当fast和slow所指的数不同的时候对slow+1重新赋值
    但是如果fast和slow相邻的时候赋值是没有必要的   [1,2,3,4]
    所以排除相邻情况 fast - slow > 1
"""

class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 1
        while (fast < len(nums)):
            if (nums[fast] != nums[slow] and fast - slow > 1): 
                slow = slow + 1
                nums[slow] = nums[fast]
            fast = fast + 1
        return slow + 1

# 我们在同一个世界吗.jpg
class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for n in nums:
            if i < 1 or n > nums[i-1]:
                nums[i] = n
                i += 1
        return i
