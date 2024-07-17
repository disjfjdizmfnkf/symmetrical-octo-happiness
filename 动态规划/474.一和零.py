class Solution:
    """
    从后往前遍历，确保更新当前状态是使用的之前已经更新过的信息
    """
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[i][m][n] 前i个子集最多有m个0和n个1的最大长度
        # dp[i][m][n] = max(dp[i-1][m][n], dp[i-1][m-c0][n-c1])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            cnt0 = cnt1 = 0
            for char in s:
                if char == '0':
                    cnt0 += 1
                else:
                    cnt1 += 1
            # 不考虑最多有0和1的个数小于当前子集中0和1的情况
            for i in range(m, cnt0 - 1, -1):
                for j in range(n, cnt1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - cnt0][j - cnt1] + 1)
        return dp[-1][-1]