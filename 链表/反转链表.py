# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        preNode = None
        while head:
            nextNode = head.next
            head.next = preNode
# 变换指针指向时，要保留对下一个节点的追踪，主打一个“用了再换”
            preNode = head
            head = nextNode
        return preNode


"""易读版本"""
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         preNode = None
#         cur = head
#         while cur:
#             nextNode = cur.next
#             cur.next = preNode
#             preNode = cur
#             cur = nextNode
#         return preNode