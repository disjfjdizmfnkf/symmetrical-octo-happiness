class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        memo = set()
        while headA:
            memo.add(headA)
            headA = headA.next
        while headB:
            if headB in memo:
                return headB
            headB = headB.next
        return None