# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode("#", head)
        pre, cur = dummy, head

        while cur:
            if cur.val != pre.val: # 如果当前数字是新出现的
                pre = pre.next
            else:
                pre.next = cur.next
            cur = cur.next
        return dummy.next