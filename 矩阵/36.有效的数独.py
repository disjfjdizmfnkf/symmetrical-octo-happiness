class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # method: 构建不同的元组来表示数字在不同维度上的出现情况 #
        # 想使用特殊的字符最好###不要用运算符### 因为运算符的优先级和结合性可能会导致不可预料的结果
        seen = set()
        for r in range(9):
            for c in range(9):
                number = board[r][c]
                if number != '.':
                    if (number, r) in seen or \
                       (number, ~c) in seen or \
                       (number, r // 3, c // 3) in seen:
                        return False
                    seen.add((number, r))
                    seen.add((number, ~c))
                    seen.add((number, r // 3, c // 3))
        return True