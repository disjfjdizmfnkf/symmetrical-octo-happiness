# 遍历DFS
class Solution1:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def bfs(r, c):
            queue = []
            queue.append((r, c))
            board[r][c] = '#'
            direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while queue:
                cr, cc = queue.pop(0)
                for dr, dc in direction:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                        board[nr][nc] = '#'
                        queue.append((nr, nc))

        if not board:
            return []

        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                isEdge = (r == 0 or c == 0 or r == rows - 1 or c == cols - 1)
                if board[r][c] == 'O' and isEdge:
                    bfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == '#':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'







#递归DFS
class Solution5:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and (r == 0 or c == 0 or r == len(board) - 1 or c == len(board[0])):
                    self.dfs(board, r, c)
                if board[r][c] == '#':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '#':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'
    def dfs(self, board, row, col):
        if (row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] == 'X'):
            return

        board[row][col] = '#'

        self.dfs(board, row + 1, col)
        self.dfs(board, row, col + 1)
        self.dfs(board, row - 1, col)
        self.dfs(board, row, col - 1)