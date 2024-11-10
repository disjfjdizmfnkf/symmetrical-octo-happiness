# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        bigger_equal = ListNode(0, None)

        less_p = dummy
        bigger_equal_p = bigger_equal

        cur = head
        while cur:
            if cur.val < x:
                less_p.next = cur
                less_p = less_p.next
            else:
                bigger_equal_p.next = cur
                bigger_equal_p = bigger_equal_p.next
            cur = cur.next
        # 连接
        less_p.next = bigger_equal.next
        bigger_equal_p.next = None  # 从最后的节点断开
        return dummy.next
