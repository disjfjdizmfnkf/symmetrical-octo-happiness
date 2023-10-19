

# 就是层序遍历
class Solution1:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            level = []
            level_leng = len(queue)
            for _ in range(level_leng):
                temp = queue.pop(0)
                level.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            res.append(level)
        return res