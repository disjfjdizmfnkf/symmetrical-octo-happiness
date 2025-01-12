class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口: 移动一个端点，在O(1)时间内保持窗口有效并且快速确定另一个端点
        hashMap = {}
        ans = l = r = 0
        for r in range(len(s)):
            if s[r] in hashMap:  # 在哈希表中不一定和现在窗口中的重复，s[r]在哈希表中但是在l之前，说明其实不是重复字符实际不在窗口中
                l = max(l, hashMap[s[r]] + 1)
            ans = max(ans, r - l + 1)
            hashMap[s[r]] = r
        return ans

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memo = set()
        res, l = 0
        for r in range(len(s)):
            # abcdeff 如果添加到第二个f,就要依次从头删除到第一个f
            while s[r] in memo:
                memo.remove(s[l])
                l += 1
            memo.add(r)
            res = max(res, r - l + 1)
        return res
