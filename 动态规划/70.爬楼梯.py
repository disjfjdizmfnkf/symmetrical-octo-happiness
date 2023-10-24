# 递归 + 记忆 aka 自顶动态规划 aka 记忆搜索
class Solution1:
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

# 动态规划 aka 自底向上
class Solution2:
    def climbStairs(self, n: int) -> int:
        f, s, res = 0, 0, 1   # 讨论边界情况 n = 1 时 res = 1
        for i in range(n):    # 从0开始到n-1
            f = s
            s = res
            res = f + s
        return res

# 矩阵快速幂  和斐波那契数列的矩阵快速幂一样
class Solution3:
    def climbStairs(self, n: int) -> int:
        def matrix_pow(a, n):
            ret = [[1, 0], [0, 1]]
            while n > 0:
                if n & 1:
                    ret = matrix_multiply(ret, a)
                n >>= 1
                a = matrix_multiply(a, a)
            return ret

        def matrix_multiply(a, b): # 2*2矩阵相乘
            c = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
            return c

        q = [[1, 1], [1, 0]]
        res = matrix_pow(q, n)
        return res[0][0]