# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:  # 返回剪枝后的树
        # 不是在原树上剪枝，而是返回剪枝后的树，和cpp引用类型不同
        # 从底部开始往上剪枝就只有两种base case，叶子节点和空节点
        if not root:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if root.val == 0 and not root.left and not root.right:
            root.val = None

        return root