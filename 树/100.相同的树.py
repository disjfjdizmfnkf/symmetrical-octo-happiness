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


# 相同的方法，只是重新写了一遍
class Solution:
    # 两个树相同 === 值相同 & 结构相同
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 对一个节点
        # 至少有一个节点为空
        if not p or not q:
            return p == q  # 判断形状是否相同
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

