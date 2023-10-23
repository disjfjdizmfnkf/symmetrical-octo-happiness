# 排序
class Solution1:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort(reverse = True)

        i, h = 0, 0
        while i < len(citations) and citations[i] > h:
            i += 1
            h += 1
        return h

# 计数排序
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = [0] * (n + 1)  # h 引用次数 分从0到n的 n+1 种情况

        for citation in citations:  # 统计 引用次数 的频次
            # 超过n的记在n上
            if citation >= n:
                count[n] += 1
            else:
                count[citation] += 1

        i = n # 要满足条件的最大h
        h = 0
        while i >= 0:
            h += count[i]  # count[i] 为引用次数为i的论文个数
            if h >= i:
                return i
            i -= 1
        return 0
