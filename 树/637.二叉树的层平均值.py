
# 层序遍历
class Solution1:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        node = [root]
        avrOfLev = [root.val]

        if not node:
            return avrOfLev

        while node:
            size = len(node)  # 上一层的节点数
            sum_ = 0
            for i in range(size):
                sum_ += node.pop(0).val
                if root.left:
                    node.append(root.left)
                if root.right:
                    node.append(root.right)
            avrOfLev.append(sum_ / size)

        return avrOfLev