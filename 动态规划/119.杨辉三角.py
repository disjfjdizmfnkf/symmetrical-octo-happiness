class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if not rowIndex:
            return []
        
        res = [[1]]

        # 从第二行到最后一行, 每行都是 i 个数
        for i in range(2, rowIndex - 1):
            res.append([1] * i)
            for j in range(1, i - 1):  # 第一个数字和最后一个数字不需要计算
                res[-1][j] = res[-2][j - 1] + res[-2][j]  # 很简单的我从哪里来
        return res                