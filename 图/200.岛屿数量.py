from typing import List
"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。
示例 1：
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
"""



# 并查集
# class Solution1:
#     def numIslands(self, grid: List[List[str]]) -> int:




# 使用BFS遍历  找到所有的岛屿
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return

        visited = set()     # 帮助分辨岛屿，输出正确的岛屿数,储存坐标
        lands = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):   # 广度优先，从点扩大到整个岛屿找到所有相连部分
            visited.add((r, c))
            queue = []    # 完成bfs，dfs要借助存储结构 否则 递归
            queue.append((r, c))
            direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while queue:
                row, col = queue.pop(0)    # 作为队列先进先出,得到row和col是为了找相邻的点
                for dr, dc in direction:
                    row, col = row + dr, col + dc
                    if (row in range(rows) and
                        col in range(cols) and
                        grid[row][col] == '1' and
                        (row, col) not in visited):
                        visited.add((row, col))
                        queue.append((row, col)) # 别忘了入栈找相邻的相邻的
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == '1':
                    bfs(r, c)
                    lands += 1
        return lands

# bfs递归
class Solution3:
    def __init__(self):
        self.rows = None
        self.cols = None

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        self.rows, self.cols, res = len(grid), len(grid[0]), 0
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    res += 1
        return res

    # 广度优先将所有连在一起的'1'都置为'0'
    def bfs(self, grid, row, col):
        if row not in range(self.rows) or col not in range(self.cols) or grid[row][col] != '1':
            return
        grid[row][col] = '0'
        self.bfs(grid, row + 1, col)
        self.bfs(grid, row - 1, col)
        self.bfs(grid, row, col + 1)
        self.bfs(grid, row, col - 1)
