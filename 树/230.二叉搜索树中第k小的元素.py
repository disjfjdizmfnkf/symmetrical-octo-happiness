# 先序遍历
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sortArray = [] 
        def preorder(root):
            if not root or len(sortArray) >= k:
                return 
            preorder(root.left)
            sortArray.append(root.val)
            preorder(root.right)
        preorder(root)
        return sortArray[k - 1]

# 迭代
class Solution1:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []  # 借助栈实现回溯
        while True:
            while root:  # 找当前最小的(当前节点的所有左边的节点)
                stack.append(root)
                root = root.left
            root = stack.pop()  # 回溯(已经到最左边或者右边的节点为空)
            k -= 1
            if not k:
                return root.val
            root = root.right


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
