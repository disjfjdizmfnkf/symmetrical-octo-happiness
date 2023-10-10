

# 递归
class Solution1:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def countHelper(root, n):
            if not root:
                return 0
            return countHelper(root.left, n) + countHelper(root.right, n) + 1
        return countHelper(root, 0)