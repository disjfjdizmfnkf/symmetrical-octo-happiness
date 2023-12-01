class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memo = {}
        res = 0
        left = 0
        for right in range(len(s)):
            if s[right] in memo:
                left = max(memo[s[right]] + 1, left)
            memo[s[right]] = right
            res = max(res, right - left + 1)
        return res

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for l in range(len(s)):
            memo = set()
            sub = 0
            for r in range(l, len(s)):
                if s[r] not in memo:
                    memo.add(s[r])
                    sub += 1
                else:
                    break
            res = max(res, sub)
        return res

