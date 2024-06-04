class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # row = [[0] * (rowIndex + 1) for _ in range(2)]
        # for i in range(rowIndex):
        #     ind = rowIndex % 2
        #     pre_ind = not ind
        #     row[ind][0] = 1
        #     for j in range(1, i + 1):
        #         row[ind][j] = row[pre_ind][j - 1] + row[pre_ind][j]
        # return row[(rowIndex-1) % 2]

        prev_row = [1]
        for i in range(1, rowIndex + 1):
            curr_row = [1] * (i + 1)
            for j in range(1, i):
                curr_row[j] = prev_row[j - 1] + prev_row[j]
            prev_row = curr_row
        return prev_row