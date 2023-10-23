# 递归 + 记忆 aka 自顶动态规划 aka 记忆搜索
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(n):
            if n <= 2:  # n = 1 一种 n = 2 两种 以n=0为基本条件也可以
                return n
            if n in memo:
                return memo[n]
            memo[n] = helper(n - 1) + helper(n - 2)
            return memo[n]
        return helper(n)