# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 高度平衡二叉树左右两个子树高度差不超过1
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        mid_index = len(nums)//2
        root = nums[mid_index]
        left_node = self.sortedArrayToBST(nums[:mid_index])
        right_node = self.sortedArrayToBST(nums[mid_index + 1:])
        node = TreeNode(root, left_node, right_node)
        return node
