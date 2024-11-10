# H指数是指： 至少 有 h 篇论文被引用次数大于等于 h
# 这里要求的就是 h

# 排序
# 方法一: h有多种不同可能的值 最优解是h可能的最大值 可知至少有两个关键变量，变化趋势相反
class Solution1:
    def hIndex(self, citations: List[int]) -> int:  # 从最大的开始找h数，从前往后引用次数在减少， h指数(满足条件的论文数)在增加
        citations.sort(reverse=True)
        h = 0
        for item in citations:
            if item > h:
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
