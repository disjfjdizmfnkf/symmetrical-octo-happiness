# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 每个节点既要提供当前深度信息(作为一边的最大长度), 还要计算这个点的最大直径
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def dfs(root):
            if not root:
                return -1
            l, r = dfs(root.left), dfs(root.right)
            ans[0] = max(ans[0], l + r + 2)
            return max(l, r) + 1
        dfs(root)
        return ans[0]
