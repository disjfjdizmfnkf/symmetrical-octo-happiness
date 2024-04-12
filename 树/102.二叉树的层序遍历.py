from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            layer = []
            layer_len = len(queue)
            for _ in range(layer_len):  # 层序遍历
                cur = queue.popleft()
                layer.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(layer)
        return res