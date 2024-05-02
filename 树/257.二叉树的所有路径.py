
# dfs 深度优先搜索 左右子树向下递归  函数的路径参数在传递时都会重新生成新的对象内存占用高
class Solution1:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def pathse(root, path):
            if not root:
                return
            path += str(root.val)
            if not root.left and not root.right:
                res.append(path)
            pathse(root.left, path + '->')
            pathse(root.right, path + '->')
        pathse(root, '')
        return res

# class Solution1_:
#     def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
#         if not root:
#             return []
#         res = []
#         self.dfs(root, "", res)
#         return res
#
#     def dfs(self, root, ls, res):
#         if not root.left and not root.right:
#             res.append(ls + str(root.val))
#         if root.left:
#             self.dfs(root.left, ls + str(root.val) + "->", res)
#         if root.right:
#             self.dfs(root.right, ls + str(root.val) + "->", res)



#迭代 + stack
class Solution2:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stack = [(root, '')]
        res = []
        while stack:
            node, path = stack.pop()  #弹出节点，加它子节点，因为我们想要的也是叶子节点的路径
            if not node.left and not node.right:
                res.append(path + str(node.val))
            if node.left:
                stack.append((node.left, path + str(node.val) + '->'))
            if node.right:
                stack.append((node.right, path + str(node.val) + '->'))
        return res