# 先排序    排序会将相关性最大最相似的从前往后排， 只用找第一个和最后一个的公共前缀
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        s, l, i = strs[0], strs[-1], 0
        while i < min(len(strs[-1]), len(strs[0])):
            if s[i] != l[i]:
                break
            i +=1
        return s[:i]