from collections import deque


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 按照一定顺序将数字到队列中，再通过想要的顺序进行赋值
        queue = deque()
        d = len(matrix)  # 注意获取的是长度
        for i in range(d):
            for j in range(d):
                queue.append(matrix[i][j])

        for i in range(d - 1, -1, -1):  # range只会遍历到第二个参数的前一个数
            for j in range(d):
                matrix[j][i] = queue.popleft()
