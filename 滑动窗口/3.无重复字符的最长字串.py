class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口: 移动一个端点，在O(1)时间内保持窗口有效并且快速确定另一个端点
        hashMap = {}
        ans = l = r = 0
        for r in range(len(s)):
            if s[r] in hashMap:
                l = max(l, hashMap[s[r]] + 1)  # 防止左边界回退
            ans = max(ans, r - l + 1)
            hashMap[s[r]] = r
        return ans

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memo = set()
        res = 0
        for r in range(len(s)):
            # abcdeff 如果添加到第二个f,就要依次从头删除到第一个f
            while s[r] in memo:
                memo.remove(s[l])
                l += 1
            memo.add(r)
            res = max(res, r - l + 1)
        return res
