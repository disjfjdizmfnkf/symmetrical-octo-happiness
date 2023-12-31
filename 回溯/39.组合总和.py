class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backTrack(combining, candidates, target):
            if target == 0:
                res.append(combining)
            if target < 0:
                return
            for i in range(len(candidates)):
                # 更新candidates为candidates[i:]，因为candidates[i]之前的元素已经被遍历组合过了
                # 有类似两重循环去重的效果
                backTrack(combining + [candidates[i]], candidates[i:], target - candidates[i])

        backTrack([], candidates, target)

        return list(res)