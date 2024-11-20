class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
         在行上判断的时候只有大于这行最大元素和小于这行最小的元素才可以决定target与这行的关系
        """
        rows, cols = len(matrix), len(matrix[0])
        target_row = -1

        top, bottom = 0, rows - 1
        while top <= bottom:
            mid = (top + bottom) // 2
            if target > matrix[mid][-1]:  # 大于这行最大的元素，确定是下面的行
                top = mid + 1
            elif target < matrix[mid][0]:  # 小于这行最小的元素，确定是上面的行
                bottom = mid - 1
            else:
                target_row = mid
                break
        if target_row == -1:
            return False

        left, right = 0, cols - 1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[target_row][mid]:
                left = mid + 1
            elif target < matrix[target_row][mid]:
                right = mid - 1
            else:
                return True
        return False