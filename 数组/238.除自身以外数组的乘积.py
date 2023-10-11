
    ####################################################################
    ########                题目要求不使用除法                      #######
    ####################################################################

# 除自身外的数相乘 == 前缀和后缀相乘
# 先将每个位置前缀的乘积储存，在乘上后缀的积（先从前往后遍历再从后往前遍历
class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):  # 从最后的下标开始，到-1(不包括)， 步长为-1
            res[i] *= postfix
            postfix *= nums[i]
        return res