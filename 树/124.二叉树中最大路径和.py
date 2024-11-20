

# 递归 nonlocal 变量
# 路径没有分叉！
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 列表是可变引用
        res = [float('-inf')]

        def dfs(node):
            if not node:
                return 0
            # 路径小于0舍弃
            l_max = max(dfs(node.left), 0)
            r_max = max(dfs(node.right), 0)
            # 优化选取每个节点都为分支时的路径
            res[0] = max(res[0], l_max + r_max + node.val)
            return node.val + max(l_max, r_max)

        dfs(root)
        return res[0]
