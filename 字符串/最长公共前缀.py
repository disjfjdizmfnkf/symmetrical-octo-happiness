
# 先排序    排序会将相关性最大最相似的从前往后排， 只用找第一个和最后一个的公共前缀
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[-1]
        res = ""
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return res           #一旦不等立即返回，节约时间
            res += first[i]
        return res