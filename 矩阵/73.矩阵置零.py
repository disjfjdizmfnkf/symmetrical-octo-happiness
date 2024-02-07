class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 想法一: 第一次遍历矩阵不能直接改变数字为0，尝试遍历两次，一次用"#"标记(标记时有额外的遍历)

        # 想法二：第一次遍历把0所在的行和列记下来，第二次遍历直接改变记录的行列
        rows, cols = len(matrix), len(matrix[0])
        seen = set()
        # 行 (r,0) : 列(c,0) 这两个类别一定要不相交 比如(0, c)也不行
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    seen.add((r, 0))
                    seen.add((~c, 0))

        for r in range(rows):
            for c in range(cols):
                if (r, 0) in seen or (~c, 0) in seen:
                    matrix[r][c] = 0
