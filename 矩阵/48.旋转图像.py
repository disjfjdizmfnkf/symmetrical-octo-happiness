from collections import deque


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 想法一：借助队列，按照某种顺序
        queue = deque()
        n = len(matrix)  # 注意作为索引时要减1
        # range 不包含最后一个
        for c in range(n):
            for r in range(n - 1, -1, -1):
                queue.append(matrix[r][c])
        for r in range(n):
            for c in range(n):
                item = queue.popleft()
                matrix[r][c] = item
