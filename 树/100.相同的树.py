# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归 树的遍历 先思考怎样解决问题之后编码
class Solution1:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None or q == None:     #base case 也是边界情况
            return p == q             #是q和p中有一个或者两个节点为空,一个为空p q不等返回false，两个为空p q相等返回true
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 
    # 不为空的时候我们需要检查三个条件
