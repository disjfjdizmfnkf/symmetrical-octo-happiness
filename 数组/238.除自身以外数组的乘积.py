# 使用前缀数组时 提前定义变量在遍历中应对边界情况
# 除自身外的数相乘 == 前缀和后缀相乘
# 先将每个位置前缀的乘积储存，在乘上后缀的积（先从前往后遍历再从后往前遍历
class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        n = n
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n - 1, -1, -1):  # start from n - 1, to -1(不包括), step -1
            res[i] *= postfix
            postfix *= nums[i]
        return res
