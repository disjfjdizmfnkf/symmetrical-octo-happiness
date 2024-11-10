
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

# 隐双指针  不是删除，而是覆盖
class Solution2:
    """这个方法巧妙的用 if i < 1 or nums[j] > nums[j-1]: 判断了元素是否为新"""
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for n in nums:
            if i < 1 or n > nums[i-1]:  #为什么不和nums[i]比？ i - 1 才是之前元素的位置，i是将来的存放位
                nums[i] = n
                i += 1  #为下一次迎接新元素准备
        return i