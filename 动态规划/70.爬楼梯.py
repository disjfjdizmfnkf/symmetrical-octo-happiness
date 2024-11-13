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

#  简单写法


class Solution:
    def climbStairs(self, n: int) -> int:
        # f(n): 爬到第n层有多少种方法 f(n) = f(n-1)+1种 + f(n-2)+1种
        f, s, res = 0, 1, 0  # 第0层: 0  第1层: 1
        for _ in range(n):
            res = f + s
            f = s
            s = res
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

        def matrix_multiply(a, b):  # 2*2矩阵相乘
            c = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
            return c

        q = [[1, 1], [1, 0]]
        res = matrix_pow(q, n)
        return res[0][0]
