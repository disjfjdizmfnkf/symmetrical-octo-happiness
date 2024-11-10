
# 记得 dummy 虚拟节点的使用 处理难应付的边界情况
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        pre, cur, temp = dummy, head, dummy
        for i in range(n - 1):
           cur = cur.next
        while cur:
            if not cur.next:
                break
            cur = cur.next
            pre = pre.next
        pre.next = pre.next.next
        return dummy.next
