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

# bfs递归 使用#标记已经访问的点而不是存储结构，节省内存
class Solution3:
    # 法一： bfs，标记经过的岛屿为其它符号(不是岛的标识)
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':  # 新的岛屿
                    res += 1
                    self.bfs(grid, r, c)
        return res

    def bfs(self, grid, row, col):
        if (row < 0 or col < 0 or row >= len(grid) or
                col >= len(grid[0]) or grid[row][col] != '1'):  # base case
            return
        grid[row][col] = '0'
        self.bfs(grid, row + 1, col)
        self.bfs(grid, row, col + 1)
        self.bfs(grid, row - 1, col)
        self.bfs(grid, row, col - 1)
