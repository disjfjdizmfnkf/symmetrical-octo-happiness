# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 递归地创造
class Solution1:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        midNum = len(nums)//2
        left = nums[:midNum]    #python []不带最后一个，就是没有含midNum
        right = nums[midNum+1:] #不含midNum

        node = TreeNode(nums[midNum])
        node.left = self.sortedArrayToBST(left)
        node.right = self.sortedArrayToBST(right)
        return node