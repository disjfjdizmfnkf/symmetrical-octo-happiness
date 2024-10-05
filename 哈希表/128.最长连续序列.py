

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 去重，将查找操作转换为O(1)
        nums = set(nums)
        best = 0
        # 从任意一个存在的连续序列的起点开始 找最长的
        for i in nums:
            if i - 1 not in nums:
                j = i
                # j = i + 1 #少算一次
                while j in nums:
                    j += 1
                best = max(best, j - i)
        return best