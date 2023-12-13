# 记住动态规划自下而上，是从子问题开始构建的，要找的那些最小的子问题，还要用它们初始化

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        L = [0] * (len(triangle) + 1)

        for i in triangle[::-1]:
            for k, v in enumerate(i):
                L[k] = v + min(L[k + 1], L[k])
        return L[0]

# 记得要画图，画完图思考子问题之间的关系，不要用那个模板解题了

# 思考逻辑模板
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        L = [0] * (len(triangle) + 1)

        for i in triangle[::-1]:
            sub_problem = [i[k] + min(L[k], L[k + 1]) for k in range(len(i))]
            L = sub_problem
        return L[0]

