from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        # f(i) = min{ f(i - j*j) + 1 }  如果i > j*j
        dp = [n] * (n + 1)
        dp[0] = 0  # 初始化
        for i in range(1, n + 1):
            for j in range(1, int(sqrt(i)) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[-1]
