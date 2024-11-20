# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.total = 0
        self.lookup = defaultdict(int)
        self.lookup[targetSum] = 1

        def dfs(node, root_sum):
            if not node:
                return
            root_sum += node.val
            self.total += self.lookup[root_sum]
            self.lookup[root_sum + targetSum] += 1
            dfs(node.left, root_sum)
            dfs(node.right, root_sum)
            self.lookup[root_sum+targetSum] -= 1

        dfs(root, 0)
        return self.total


class Solution2:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0

        # 从每个节点上开始累加路径和
        def helper(root, cur):
            if not root:
                return
            helper(root.left, cur + root.val)
            helper(root.right, cur + root.val)
            if cur + root.val:
                self.res += 1

        def bfs(root):
            if not root:
                return
            help(root, 0)
            bfs(root.left)
            bfs(root.right)

        bfs(root)
        return self.res
