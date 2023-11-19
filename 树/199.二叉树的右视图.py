
# 借助queue 按层遍历
class Solution1:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = []
        if root:   # 考虑一开始root为空的情况
            queue.append(root)
        while queue:
            layerLen = len(queue)
            for i in range(layerLen):
                cur = queue.pop(0)
                if i == layerLen - 1:
                    res.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return res

class Solution3:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        q = [(root, 0)]
        for node, level in q:
            if level == len(res):
                res.append(node.val)
            if node.right:
                q.append((node.right, level + 1))
            if node.left:
                q.append((node.left, level + 1))

        return res

# 递归
class Solution2:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root, depth):
            if not root:
                return
            if depth == len(res):
                res.append(root.val)
            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)
        dfs(root, 0)
        return res
