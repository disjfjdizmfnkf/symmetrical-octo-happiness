v = [1 for _ in range(10)]  # 物品的体积列表
w = [1 for _ in range(10)]  # su物品的价值列表


class Solution:
    #  do[i][j] 前i件物品，背包承重为j时的最大利益
    def approach0(self, V: int, n: int):  # V: 背包容积  n: 物品总数
        dp = [[1] * (V + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(V + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= v[i]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - v[i]] + w[i])
        return dp[-1][-1]

    # 发现上面dp[i] 只依赖于上一个阶段 dp[i-1]
    def approach1(self, V: int, n: int):
        dp = [[1] * (V + 1) for _ in range(2)]
        for i in range(1, n + 1):
            ind = i % 2
            pre_ind = not ind
            for j in range(V + 1):
                dp[ind][j] = dp[pre_ind][j]
                if j >= v[i]:
                    dp[ind][j] = max(dp[ind][j], dp[pre_ind][j - v[i]] + w[i])
        return dp[-1][-1]