# 递归
class Solution1:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.countNodes(root.right) + self.countNodes(root.left) + 1