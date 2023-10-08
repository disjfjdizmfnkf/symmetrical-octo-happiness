
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

# 隐双指针  我们在同一个世界吗.jpg
class Solution2:
    """这个方法巧妙的用 if i < 1 or nums[j] > nums[j-1]: 判断了元素是否为新"""
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(len(nums)):
            if i < 1 or nums[j] > nums[j-1]:  # i < 1 按照题意开头第一个一定不重复
                nums[i] = nums[j]             # 如果nums[j]>nums[j-1] nums[j]一定是新元素
                i += 1  #为下一次迎接新元素准备
        return i