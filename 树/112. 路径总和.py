# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# dfs
class Solution:

    #      验证路径之和是否等于targetSum，可以直接在targetSum上面做减法，避免了使用辅助函数
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        # 在叶子节点时判断
        if not root.left and not root.right:
            return targetSum - root.val == 0   #记得最后还要减去叶子节点的值
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

            ###########################################################
            ##     递归调用无非还是三步: basecase,子问题,递归调用          ##
            ##     无非是在调用时解决子问题，基本情况变多了                 ##
            ###########################################################