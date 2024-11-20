class Solution1:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        l, t, r, b = 0, 0, len(matrix[0]) - 1, len(matrix) - 1
        res = []
        while True:
            # 向右遍历
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            t += 1
            if t > b:
                break
            # 向下遍历
            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r -= 1
            if l > r:
                break
            # 向左遍历
            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])
            b -= 1
            if b < t:
                break
            #
            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break
        return res

# 不断从前往后遍历一个列表 使用一个额外的变量实现


class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])
        visited = set()
        res = []
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direct_index = 0  # 实现反复遍历directions数组
        r, c = 0, 0
        for _ in range(rows * cols):
            visited.add((r, c))
            res.append(matrix[r][c])

            next_r = r + directions[direct_index][0]
            next_c = c + directions[direct_index][1]

            # 切换方向的条件
            if (next_r < 0 or next_c < 0
                    or next_r >= rows or next_c >= cols
                    or (next_r, next_c) in visited):
                direct_index = (direct_index + 1) % 4

            r += directions[direct_index][0]
            c += directions[direct_index][1]

        return res
