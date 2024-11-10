# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#递归
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        if head.val != val:
            head.next = self.removeElements(head.next, val)
            return head
        else: #为要删除的节点
            return self.removeElements(head.next, val)#直接递归调用，并没有把这次head连接起来相当于删除

