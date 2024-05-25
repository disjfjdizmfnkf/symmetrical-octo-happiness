"""
给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。
"""


#  是在原来的树上修改

# 递归  因为链表展开的顺序是先序遍历的顺序，所以想最后一个节点，我们把他接到前一个节点的右子树上，
# 然后再把前一个节点接到当前节点的右子树上，递归的这样做，最后就能得到一个展开的链表
class Solution1:  # 将先序遍历的子节点变为右子节点
    def __init__(self):
        self.prev = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        # 先向右再向左，因为加节点是从后往前加的
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root
