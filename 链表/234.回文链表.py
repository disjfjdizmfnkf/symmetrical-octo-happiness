# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        i, j = head, head
        while j and j.next:
            stack.append(i)
            i = i.next
            j = j.next.next
        if j:
            i = i.next
        while stack:
            cur = stack.pop()
            if cur.val != i.val:
                return False
            i = i.next
        return True