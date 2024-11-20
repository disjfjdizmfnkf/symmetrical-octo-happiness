
# 动态规划
class Solution:
    def wordBreak(self, s: str, wordDict: List[str], memo={}) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):  # 遍历字符串的每个位置
            for word in wordDict:
                word_len = len(word)
                # 我从哪里来, 但是因为会没有必要的频繁访问dp列表，所以这样写
                if i >= word_len and dp[i - word_len] and s[i - word_len:i] == word:
                    dp[i] = True
        return dp[-1]


# 记忆递归 更容易想到
class Solution1:
    def wordBreak(self, s: str, wordDict: List[str], memo={}) -> bool:
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
        for i in range(len(s) - 1, -1, -1):  # 寻找子问题
            for word in wordDict:
                if word == s[i:i+len(word)] and (len(word) + i) <= len(s):
                    dp[i] = dp[i + len(word)]
                if dp[i]:  # 已经找到了
                    break
        return dp[0]
