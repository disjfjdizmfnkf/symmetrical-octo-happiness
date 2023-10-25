
# 迭代
class Solution1:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            while root: # 一直向左走
                stack.append(root)
                root = root.left
            root = stack.pop() # 走到头了，出栈
            k -= 1
            if k == 0:
                return root.val
            root = root.right # 向右走一步


# 递归 + 剪枝
# 使用一个全局变量(类的成员变量)）记录当前节点的排名
class Solution2:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = None
        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
                return
            inOrder(root.right)
        inOrder(root)
        return self.res


# 一般的递归
class Solution3:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            res.append(root.val)
            inOrder(root.right)
        inOrder(root)
        return res[k - 1]