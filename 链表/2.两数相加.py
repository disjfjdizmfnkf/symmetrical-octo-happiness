
# 遍历

class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 注意进位是十位, 使用 // floor division 获得商
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            sum_ = carry
            if l1:
                sum_ += l1.val
                l1 = l1.next
            if l2:
                sum_ += l2.val
                l2 = l2.next
            cur.next = ListNode(sum_ % 10)
            carry = sum_ // 10
            cur = cur.next
        return dummy.next
