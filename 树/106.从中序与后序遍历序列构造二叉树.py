class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def myBuildTree(inorder_left: int, inorder_right: int, postorder_left: int, postorder_right: int):
            if inorder_left > inorder_right:
                return None

            # 后序遍历中的最后一个节点就是根节点
            postorder_root = postorder_right
            # 在中序遍历中定位根节点
            inorder_root = index[postorder[postorder_root]]

            # 先把根节点建立出来
            root = TreeNode(postorder[postorder_root])
            # 得到右子树中的节点数目
            size_right_subtree = inorder_right - inorder_root
            # 递归地构造右子树，并连接到根节点
            # 后序遍历中「从 右边界-右子树节点数目 开始到 右边界-1」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(inorder_root + 1, inorder_right, postorder_right - size_right_subtree,
                                     postorder_right - 1)
            # 递归地构造左子树，并连接到根节点
            # 后序遍历中「从 左边界 开始到 右边界-右子树节点数目-1」的元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(inorder_left, inorder_root - 1, postorder_left,
                                    postorder_right - size_right_subtree - 1)
            return root

        n = len(inorder)
        # 构造哈希映射快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)