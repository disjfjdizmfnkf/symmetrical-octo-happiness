

# 递归 nonlocal 变量
# 路径没有分叉！
class Solution:
    """
    在这个问题中，答案是需要最大路径，
    需要递归解决的确是（返回没有分支的子树的最大路径）
    所以递归函数不一定可以直接解决问题，所以需要辅助函数和全局变量
    总之每次调用的子问题做两件事：
    1.返回以当前调用节点分叉的最大路径
    2.返回以当前节点为不分叉的最大路径
    """

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = [float('-inf')]

        def helper(node):  # why use helper function?   to return res
            if not node:  # 辅助函数的作用是返回以当前节点为根节点的最大路径，并且更新全局变量
                return 0
            leftMax = max(helper(node.left), 0)
            rightMax = max(helper(node.right), 0)
            maxSum[0] = max(maxSum[0], leftMax + rightMax + node.val)
            return max(leftMax, rightMax) + node.val  # 只能选一个方向

        helper(root)
        return maxSum[0]