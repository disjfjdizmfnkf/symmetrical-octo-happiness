
# 递归解法
class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        while not preorder or not inorder:
            return

        root = TreeNode(preorder[0])

        i = 0  # 根在中序列表中的位置
        while inorder[i] != preorder[0]:
            i += 1
        root.left = self.buildTree(preorder[1:1 + i], inorder[:i])
        root.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
        return root