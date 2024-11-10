class Solution:
    def is_palindrome(self, s, i, j):
        while i <= j:
            if s[i] != s[j]:
                return False
            i, j = i + 1, j - 1
        return True

    def minCut(self, s: str) -> int:
        # f为最少分割次数，因变量为i（以i位置结尾的最少分割次数）
        n = len(s)
        # 这里长度为i最多分割i-1次, 也可以用达不到的最大值
        dp = [ i - 1 for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i):  # 回文串开始位置
                if self.is_palindrome(s, j, i - 1):
                    dp[i] = min(dp[i], dp[j] + 1)  # 滚动数组
        return dp[n]