class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        size = len(board)
        def count_position(ID):
            r = size - 1 - (ID - 1) // size
            # ?????为什么不能用r的奇偶判断???
            c = (ID - 1) % size if (size - 1 - r) % 2 == 0 else size - 1 - (ID - 1) % size
            return [r, c]
        # board.reverse()
        # def count_position(ID):
        #     r = (ID - 1) // size
        #     c = (ID - 1) % size
        #     if r % 2:
        #         c = size - 1 - c
        #     return [r, c]
        q = deque()
        q.append([1, 0])  # [currID, count_moves]
        visit = set()
        while q:
            currID, moves = q.popleft()

            for i in range(1, 7):
                nextID = currID + i
                r, c = count_position(nextID)
                if board[r][c] != -1:
                    nextID = board[r][c]
                if nextID == size * size:
                    return moves + 1
                if nextID not in visit:
                    visit.add(nextID)
                    q.append([nextID, moves + 1])
        return -1
