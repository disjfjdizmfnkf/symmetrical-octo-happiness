# 先排序    排序会将相关性最大最相似的从前往后排， 只用找第一个和最后一个的公共前缀
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        sortest = strs[0]
        longest = strs[-1]
        res = ""
        for i in range(len(sortest)):
            if sortest[i] == longest[i]:
                res += sortest[i]
            else:
                return res
        return res