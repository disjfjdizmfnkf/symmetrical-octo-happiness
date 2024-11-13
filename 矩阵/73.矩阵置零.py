
# 改进方法
class Solution1:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r, c = len(matrix), len(matrix[0])
        memo = set()
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    # 不能添加(i, 0) (0, j) 靠位置不能完全区分行和列，因为0的特殊情况
                    memo.add((0, i))
                    memo.add(('~', j))
        for i in memo:
            if not i[0]:
                for j in range(c):
                    matrix[i[1]][j] = 0
            else:
                for j in range(r):
                    matrix[j][i[1]] = 0

class Solution2:
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
