# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target
# 的那两个整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            complement = target - nums[i]
            # 不用考虑前面的元素，后面的元素必定和前面的加过了
            if (complement in nums[i+1:]):
                return [i, nums[i+1:].index(complement) + i + 1]

 
# hashMap
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = dict()
        for i, num in enumerate(nums):  # enumrate() 同时遍历索引和值
            if target - num in hashMap:
                return [hashMap[target - num], i]
            hashMap[nums[i]] = i  # 字典和hashTable一样 value ---对应--- key
