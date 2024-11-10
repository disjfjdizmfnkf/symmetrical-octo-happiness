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

    class Solution:
        def sumNumbers(self, root: Optional[TreeNode]) -> int:
            res = []

            def dfs(root, num):
                if not root.left and not root.right:
                    res.append(int(num + str(root.val)))
                    return
                if root.left: dfs(root.left, num + str(root.val))
                if root.right: dfs(root.right, num + str(root.val))

            dfs(root, "")
            return sum(res)

# 使用字符串传递
class Solution2:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def dfs(root, num):
            if not root.left and not root.right:
                res.append(int(num + str(root.val)))
                return
            if root.left: dfs(root.left, num + str(root.val))
            if root.right: dfs(root.right, num + str(root.val))
        dfs(root, "")
        return sum(res)

# 对于这道题的特解(传递数字)
class Solution3:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def dfs(root, num):
            if not root.left and not root.right:
                res.append(num*10 + root.val)
                return
            if root.left: dfs(root.left, num*10 + root.val)
            if root.right: dfs(root.right, num*10 + root.val)
        dfs(root, "")
        return sum(res)