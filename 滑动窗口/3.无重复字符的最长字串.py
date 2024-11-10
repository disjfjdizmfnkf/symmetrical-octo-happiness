class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口: 移动一个端点，在O(1)时间内保持窗口有效并且快速确定另一个端点
        hashMap = {}
        ans = l = r = 0
        for r in range(len(s)):
            if s[r] in hashMap:  # keep left is valid
                l = max(l, hashMap[s[r]] + 1)  # 这里使用max确保左边界不回退
            ans = max(ans, r - l + 1)
            hashMap[s[r]] = r
        return ans

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

