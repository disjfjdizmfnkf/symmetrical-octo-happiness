# bfs 变形 按层处理元素
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bankSet = set(bank)
        options = ['A', 'C', 'G', 'T']
        queue = deque()
        queue.append(startGene)
        visited = set()
        visited.add(startGene)
        count = 0

        while queue:
            size = len(queue)
            for i in range(size):  # 按层处理元素，类比树的层序遍历
                gene = queue.popleft()
                if gene == endGene:
                    return count
                for j in range(8):
                    for option in options:
                        newGene = gene[:j] + option + gene[j + 1:]
                        if newGene in bankSet and newGene not in visited:
                            visited.add(newGene)
                            queue.append(newGene)
            count += 1

        return -1