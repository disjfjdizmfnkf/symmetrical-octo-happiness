

# 想到了没敢继续想下去
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tail = dummy
        length = 0

        while tail.next:
            length += 1
            tail = tail.next
        if length == 0 or length == k:
            return head
        new_head = dummy.next
        tail.next = new_head
        k = k % length
        for i in range(length - k - 1):
            new_head = new_head.next
        dummy.next = new_head.next
        new_head.next = None
        return dummy.next

class Solution2:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        dummy = ListNode(0, head)
        pre = dummy
        length = 0
        tail = head
        while tail:
            length += 1
            tail = tail.next

        k = k % length
        if length == 1 or k == length or k == 0:
            return head
        for i in range(k - 1):
            head = head.next

        while head.next:
            head = head.next
            pre = pre.next
        head.next = dummy.next
        dummy.next = pre.next
        pre.next = None
        return dummy.next