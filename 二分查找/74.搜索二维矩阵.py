class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        # 二维的矩阵就用两个方向上的binSearch
        top, bottom = 0, rows - 1
        # target_row = 0
        # while top <= bottom:
        #     m = bottom + (top - bottom) // 2
        #     if matrix[m][cols - 1] > target:
        #         bottom = m - 1
        #     elif matrix[m][cols - 1] <= target:
        #         target_row = m
        #         top = m + 1
        target_row = -1
        while top <= bottom:
            m = top + (bottom - top) // 2
            if matrix[m][cols - 1] < target:  # 让top逼近target，top不会超过target行
                top = m + 1
            else:
                target_row = m  # 否则目标行在m或者m的上面
                bottom = m - 1  # 逼近目标行
        if target_row == -1:
            return False

        l, r = 0, cols - 1
        while l <= r:
            m = l + (r - l) // 2
            if matrix[target_row][m] > target:
                r = m - 1
            elif matrix[target_row][m] < target:
                l = m + 1
            else:
                return True
        return False