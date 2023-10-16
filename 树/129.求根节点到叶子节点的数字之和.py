# 对一个二叉树，求从根节点到叶子节点的数字之和

# 第一种递归
class Solution1:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, Sum):
            if not node:
                return 0

            Sum = Sum * 10 + node.val  # 为什么先算？ 提示：下面代码
            if not node.left and not node.right:
                return Sum
            return dfs(node.left, Sum) + dfs(node.right, Sum)
        return dfs(root, 0)