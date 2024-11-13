# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 使用memo记录节点, 关注节点本身而不是节点值
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        memo = set()
        while head:
            if head in memo:
                return head
            memo.add(head)
            head = head.next
        return None
