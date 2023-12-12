# 记忆递归 更容易想到
class Solution1:
    def wordBreak(self, s: str, wordDict: List[str], memo = {}) -> bool:
        if not s:
            return True
        if s in memo:
            return memo[s]
        for word in wordDict:
            length = len(word)
            if word == s[0:length]:
                if self.wordBreak(s[length:], wordDict, memo):
                    memo[s] = True
                    return True
        memo[s] = False
        return False

# 动态规划建表格
class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1): # 寻找子问题
            for word in wordDict:
                if word == s[i:i+len(word)] and (len(word) + i) <= len(s):
                    dp[i] = dp[i + len(word)]
                if dp[i]:  # 已经找到了
                    break
        return dp[0]