

# 递归 nonlocal 变量
class Solution1:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')  # 全局最大路径和的初始值

        def maxPathSumHelper(node):
            nonlocal max_sum  # 引用外部的 max_sum 变量

            if not node:
                return 0

            # 递归计算左右子树的最大路径和，并取其中较大的一个
            # 和0比较是因为我们尽量让路径增加( > 0)而不是减少
            left_sum = max(maxPathSumHelper(node.left), 0)
            right_sum = max(maxPathSumHelper(node.right), 0)

            # 更新全局最大路径和
            max_sum = max(max_sum, node.val + left_sum + right_sum)

            # 返回以当前节点为起点的最大路径和（只能选择左子树或右子树的一条路径）
            return node.val + max(left_sum, right_sum)

        maxPathSumHelper(root)  # 调用辅助函数开始计算

        return max_sum