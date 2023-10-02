# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




        ####################################
        #  怎么想到用辅助函数? 对称的判断条件?   #
        ####################################


# 递归
class Solution1:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSymmetricHelper(left, right):
            if not left or not right:  #左右节点必须形状上先对称
                return left == right
            return left.val == right.val and isSymmetricHelper(left.left,right.right) and isSymmetricHelper(left.right, right.left)
        return isSymmetricHelper(root.left, root.right)


# stack
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool: