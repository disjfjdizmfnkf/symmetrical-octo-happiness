

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
# DFS
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """"l_max 和 r_max 是没有左子树分支的最大值，并且一开始就要与0比较，不能在res[0]中比较，那样就算res[0]对了,
        l_max 和 r_max 也还是错的"""
        res = [float('-inf')]

        def dfs(node):
            if not node:
                return 0
            l_max = max(dfs(node.left), 0)
            r_max = max(dfs(node.right), 0)
            res[0] = max(res[0], l_max + r_max + node.val)
            return node.val + max(l_max, r_max)

        dfs(root)
        return res[0]