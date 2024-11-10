class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]  # 记录已访问的单元格

        def dfs(r, c, index):
            # 如果单词的所有字母都匹配完了，说明找到了符合条件的路径
            if index == len(word):
                return True

            # 判断当前位置是否越界，或者当前位置已经访问过，或者当前位置的字母不匹配
            if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or board[r][c] != word[index]:
                return False

            visited[r][c] = True  # 标记当前位置为已访问

            # 在上、下、左、右四个方向上继续搜索
            if dfs(r - 1, c, index + 1) or \
                    dfs(r + 1, c, index + 1) or \
                    dfs(r, c - 1, index + 1) or \
                    dfs(r, c + 1, index + 1):
                return True

            visited[r][c] = False  # 回溯，重置当前位置的访问状态
            return False

        # 遍历整个二维网格，找到起点位置开始搜索
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False