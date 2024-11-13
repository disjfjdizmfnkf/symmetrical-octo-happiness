
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre = [None]  # 使用列表，在下面函数内修改值不会改变其引用，如果是变量就会修改引用
        def flatten_helper(root):
            if not root:
                return

            flatten_helper(root.right)
            flatten_helper(root.left)

            root.right = pre[0]
            root.left = None
            pre[0] = root

        flatten_helper(root)


class Solution2:  # 将先序遍历的子节点变为右子节点
    def __init__(self):
        # 保存上一个处理的节点
        self.prev = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        # 先递归的展开右子树，再展开左子树，
        # 这样做保证处理当前节点时右子树已经被展开了
        self.flatten(root.right)
        self.flatten(root.left)

        # 当前节点的右子树就是之前已经展开的
        root.right = self.prev
        root.left = None

        # 在下次递归调用中使用这次的root作为prev
        self.prev = root
