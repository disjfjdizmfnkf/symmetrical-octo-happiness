from typing import List


########################################################################################################
#  1.确定递推状态(递推公式中f(n)的含义)
#  2.确定递推公式:f(x)和哪些f(y)
#  3.分析边界条件
#  4.动态规划就是多了一个决策过程
########################################################################################################


class Solution:
    # f(n)代表到前n家获取的最大值；f(n) = max(f(n-1),  f(n-2) + gain)
    def rob0(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0], dp[1] = 0, nums[0]
        for i in range(2, n + 1):  # range不包含最后一个n+1
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])  # nums[i-1]：i-1是第n家的索引
        return dp[n]

    # rob0优化
    def rob1(self, nums: List[int]) -> int:
        rub1, rub2 = 0, 0
        # [rub1, rub2, n, n+1, ...]
        for n in nums:
            temp = max(rub1 + n, rub2)  # temp 为可偷到的最大金额 rub1 + n 为偷当前房子，rub2 为不偷当前房子 只有这两种情况
            rub1 = rub2
            rub2 = temp
        return rub2


# 递归
# 返回p之后可以强到的最大金额
class Solution1:
    def rob0(self, nums: List[int]) -> int:
        def helper(nums, p):
            if p >= len(nums):
                return 0
            return max(nums[p] + helper(nums, p + 2), helper(p + 1))  # 画出决策树 只有抢和不抢当前的两种情况

        return helper(nums, 0)

    # 递归 + 记忆 优化
    def rob1(self, nums: List[int]) -> int:
        memo = {}

        def helper(nums, p):
            if p >= len(nums):
                return 0
            if p in memo:
                return memo[p]
            memo[p] = max(nums[p] + helper(nums, p + 2), helper(p + 1))
            return memo[p]

        return helper(nums, 0)
