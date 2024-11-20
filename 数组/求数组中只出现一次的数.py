"""假设数组中一定会有一个单独的元素 其他的元素都为偶数个"""

# hashMap
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap = dict()
        for i in nums:
            hashMap[i] = hashMap.get(i, 0) + 1  # get 返回值为value 默认返回值0

        for k, v in hashMap.items():  # dict.items() 返回一个类似于列表的对象，
            if v == 1:  # 其中每个元素都是形如 (key, value) 的元组
                return k


# 异或运算，相同为0不同为1：
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans ^= i
        return ans


# 数学方法 + set 相关知识
class Solution3:
    def singleNumber(self, nums: List[int]) -> int:
        return sum(set(nums))*2 - sum(nums)    #nums数组可以直接转化为set,set中的元素是没有重复的 