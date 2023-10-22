# 计数排序
class Solution1:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort(reverse = True)

        i, h = 0, 0
        while i < len(citations) and citations[i] > h:
            i += 1
            h += 1
        return h
