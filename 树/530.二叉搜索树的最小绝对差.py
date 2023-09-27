# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 中序遍历
class Solution1:
    def inOder(self, root: TreeNode, res):
        if not root:
            return
        self.inOder(root.right, res)
        res.append(root.val)
        self.inOder(root.left, res)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = []
        minNum = float('inf')
        self.inOder(root, res)
        for i in range(len(res)-1):
            minNum = min(minNum, abs(res[i] - res[i+1]))
        return minNum
 