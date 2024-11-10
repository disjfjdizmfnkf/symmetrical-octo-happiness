
# 基本解题方法
class Solution:
    # 从下往上 递推状态f(i, j)的含义描述：从下往上到位置(i, j) 的最短路径
    # f(i, j) = min(f(i+1, j), f(i+1, j+1)) + cost(i, j)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * n for _ in range(2)]
        dp[(n - 1) % 2] = triangle[-1] # 边界:最底层  滚动数组:使用层数的索引切换
        for i in range(n - 2, -1, -1):  # n层(倒退 计算第二次n = 1)
            ind = i % 2
            next_ind = not ind  # 使用索引计算可能会溢出
            for j in range(i + 1):  # 遍历一个正三角
                dp[ind][j] = min(dp[next_ind][j], dp[next_ind][j + 1]) + triangle[i][j]
        return dp[0][0]  # 三角形顶部 滚动索引0%2 = 0








class Solution1:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        L = [0] * (len(triangle) + 1)

        for i in triangle[::-1]:
            sub_problem = [i[k] + min(L[k], L[k + 1]) for k in range(len(i))]
            L = sub_problem
        return L[0]


class Solution2:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        L = [0] * (len(triangle) + 1)

        for i in triangle[::-1]:
            for k in range(len(i)):
                L[k] = i[k] + min(L[k], L[k + 1])
        return L[0]


