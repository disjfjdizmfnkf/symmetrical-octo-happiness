# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归
class Solution1:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


# 层序遍历
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        queue = [root]         # 先把root放入 辅助队列

        while queue:
            temp = queue.pop(0)  # 弹出第一个，将其左右节点置换
            temp.left, temp.right = temp.right, temp.left
            if temp.left:  # 如果他有子节点，把子节点加入队列，继续操作
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return root
