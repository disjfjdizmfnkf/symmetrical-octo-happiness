
#取巧
class Solution1:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        #需要初始化
        res = [[1]]
        while len(res) < numRows:
            newRow = [a + b for a,b in zip([0]+res[-1], res[-1]+[0])]
            res.append(newRow)
        return res

#动态规划 math方法
#不想写力