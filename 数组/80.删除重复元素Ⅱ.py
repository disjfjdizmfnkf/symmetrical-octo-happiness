# 素组是排好序的，超过两个的相同元素只保留两个
# [0,0,1,1,1,1,2,3,3]  --> [0,0,1,1,2,3,3]


# ???
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        brush_index = 0  # 唯一一个对原数组操作的指针 像一个魔法刷子
        for n in nums:
            # 如果这个数字没有出现过两次
            if brush_index < 2 or n != nums[brush_index - 2]:
                nums[brush_index] = n  # 存放新元素
                brush_index += 1  # 存放位置后移 为下一个做准备
        return brush_index
