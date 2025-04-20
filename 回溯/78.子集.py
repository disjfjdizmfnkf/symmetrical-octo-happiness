class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backTrack(combine, start):
            res.append(combine)  # append修改元素组没有返回值
            for i in range(start, len(nums)):
                backTrack(combine + [nums[i]], i + 1)
        backTrack([], 0)
        return res 

