from typing import List


# 因为数组中还有负数，所以正负都要记录
class Solution:
    def maxProduct(self, nums: List[int]) -> int:  # f(n) 代表以第n位结尾的子数组的最大值
        ans, max_sum, min_sum = float('-inf'), 1, 1
        for i in nums:
            if i < 0:  # 负数会改变最大值的正负 最小值也可能变成最大值
                max_sum, min_sum = min_sum, max_sum
            max_sum = max(max_sum * i, i)
            min_sum = min(min_sum * i, i)
            ans = max(max_sum, ans)  # 将求解过程放入遍历过程中等于使用数组时求数组中的最大值
        return ans

    # 两个f(n) 一个表示以n结尾的成数最小子数组，一个表示乘数最大 因为数组中的负数会影响正负
    def maxProduct1(self, nums: List[int]) -> int:  # f(n) 代表以第n位结尾的子数组的最大值
        # 注意这两个是两个不同的数组
        n = len(nums)
        min_dp, max_dp = [1] * (n + 1), [1] * (n + 1)
        for i in range(1, n + 1):
            min_dp[i] = min(min_dp[i - 1] * nums[i - 1], max_dp[i - 1] * nums[i - 1], nums[i - 1])
            max_dp[i] = max(min_dp[i - 1] * nums[i - 1], max_dp[i - 1] * nums[i - 1], nums[i - 1])
        return max(max_dp[1:])