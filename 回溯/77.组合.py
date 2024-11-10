# 递归回溯
class Solution1:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backTrack(combination, n, k):
            if k == 0 :
                res.append(combination)
            if n == 0:
                return
            while n > 0:
                backTrack(combination + [n], n - 1, k - 1)
                n -= 1
        backTrack([], n, k)
        return res

# 运用python的内置函数
class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n+1), k))