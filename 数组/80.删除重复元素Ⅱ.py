
# 素组是排好序的，超过两个的相同元素只保留两个
# [0,0,1,1,1,1,2,3,3]  --> [0,0,1,1,2,3,3]


# 类双指针
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0   # i是存放目标元素的位置(这里指新出现的元素)
        for num in nums:
            if i < 2 or num > nums[i-2]: # 出现新元素的情况
                nums[i] = num   # 存放新元素
                i += 1          # 存放位置后移 为下一个做准备
        return i
