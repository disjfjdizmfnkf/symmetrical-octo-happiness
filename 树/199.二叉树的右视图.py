
# 层序遍历，每层的最后一个就是最右边看到的
class Solution1:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        res = []
        que = deque()
        que.append(root)
        while que:
            n = len(que)
            res.append(que[n - 1].val)
            for _ in range(n):
                cur = que.popleft()
                l, r = cur.left, cur.right
                if l: que.append(l)
                if r: que.append(r)
        return res

# 别样的层序遍历
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
