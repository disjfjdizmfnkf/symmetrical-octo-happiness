class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # f是公共子序列长度, 自变量是text1被看见的长度和text2的被看见的长度（前i/j位）
        l1, l2 = len(text1), len(text2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        # 自变量变化
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                # 我从哪里来  此时dp[i][j]还是未求出的
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
