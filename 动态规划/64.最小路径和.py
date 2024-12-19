class Solution:
    # 一行一行遍历求每个位置
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 计算边界上的每个点到起点的开销，之后每个空格都可以计算出来
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        
        # 根据 左边和上边计算当前位置的最小花费
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]