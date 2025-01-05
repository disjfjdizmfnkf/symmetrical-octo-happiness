class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backTrack(combine, start, total):
            if target == total:
                res.append(combine)
                return
            if total < target:
                for i in range(start, len(candidates)):
                    # 新的组合无视顺序，只要元素相同就会被当成是一个组合
                    # 使用start作为当前位置标记，挑选当前及之后的数字
                    backTrack(combine + [candidates[i]], i, total + candidates[i])
        backTrack([], 0, 0)
        return res

class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combine = []
        def backTrack(start, total):
            if target == total:
                res.append(combine[:])
                return
            if total < target:
                for i in range(start, len(candidates)):
                    combine.append(candidates[i])
                    backTrack(i, total + candidates[i])
                    combine.pop()  # 当前层递归结束后，恢复之前的状态
        backTrack(0, 0)
        return res
