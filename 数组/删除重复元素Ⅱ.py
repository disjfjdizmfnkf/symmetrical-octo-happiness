
# 素组是排好序的，超过两个的相同元素只保留两个
# [0,0,1,1,1,1,2,3,3]  --> [0,0,1,1,2,3,3]


# 类双指针 我们在同一个世界吗.jpg
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            if i < 2 or num > nums[i-2]: #nums[i-2] 指的是前面应该排好序的元素
                nums[i] = num   #如果num>nums[i-2]说明此时num等于前面
                i += 1
        return i

"""
   这个方法和双指针的核心一样,num向后遍历所有元素(像fast指针),i用来写结果数组(像slow指针)
   理解的难点和双指针也一样,重点在什么时候写( num>nums[i-2] ),在哪儿写
   我们是不是可以考虑有两个数组的存在(实际只有一个)?
   一个为fast遍历读取
   一个为slow创造的res数组
"""