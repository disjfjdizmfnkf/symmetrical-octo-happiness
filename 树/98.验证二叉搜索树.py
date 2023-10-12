# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 递归 辅助函数
"""
            不能只考虑单个根节点和左右子节点的关系，还要考虑整个左子树和右子树的值都满足二叉搜索树的要求。
         整个左子树的值都小于根节点的值，并且整个右子树的值都大于根节点的值。
"""
def isValidBST(root: TreeNode) -> bool:
    def helper(root, lower, upper):
        if not root:
            return True
        if root.val <= lower or root.val >= upper: # 注意不能等于
            return False
        # 每次递归调用，我们都将不同的上界(右)和下界(左)传递到递归子树中，因为我们往一边走改变另一半的范围，所以我们可以真确限制子树的范围
        # 左右墙壁(上下界)一直都会被传递，更新时会使之缩小范围
        return helper(root.left, lower, root.val) and helper(root.right, root.val, upper)
    return helper(root, float('-inf'), float('inf'))