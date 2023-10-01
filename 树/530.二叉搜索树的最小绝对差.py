# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 中序遍历 （从小到大）
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
        self.inOder(root, res)  #中序遍历的顺序是由小到大遍历的，添加元素的顺序自然也是
        for i in range(len(res)-1):  # 因为列表中的数是升序排列的
            minNum = min(minNum, abs(res[i] - res[i+1]))
        return minNum