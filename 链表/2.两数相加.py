
# 遍历

class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 初始化结果数组，头节点是空节点
        dummy = ListNode()
        cur = dummy
        # 初始化进位
        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            value = l1_val + l2_val + carry
            carry = value//10
            value = value%10
            cur.next = ListNode(value) # 注意这里是cur.next，因为cur是空节点

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            # 注意返回dummy.next，因为dummy是一个空节点
        return dummy.next