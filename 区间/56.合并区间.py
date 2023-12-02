class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        # 对区间进行排序
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= merged[-1][1]:
                # 如果当前区间与前一个合并后的区间重叠，进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                # 如果没有重叠，将当前区间添加到合并后的区间列表
                merged.append(interval)
        return merged