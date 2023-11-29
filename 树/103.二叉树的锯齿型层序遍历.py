# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        flag = 1     # 1表示从左往右 -1表示从右往左
        res = []
        while queue:
            layerLen = len(queue)
            layer = []
            for _ in range(layerLen):
                if flag == 1: # 从左往右入队
                    cur = queue.popleft()
                    layer.append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                else: # 从右往左入队
                    cur = queue.pop()
                    layer.append(cur.val)
                    if cur.right:
                        queue.appendleft(cur.right)
                    if cur.left:
                        queue.appendleft(cur.left)
            res.append(layer)
            flag *= -1
        return res