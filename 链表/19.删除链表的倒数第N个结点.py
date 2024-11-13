
# 记得 dummy 虚拟节点的使用 处理难应付的边界情况
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        # 实际删除要找到要删除节点的前一个节点，所以end要多走一步，二者距离要增加1
        f_pre_del, f_end = dummy, head
        # 在没链表的长度内用f_end拉开距离
        while f_end and n:
            f_end = f_end.next
            n -= 1
        # 二者同时走，距离保持不变，直到f_end到结尾
        while f_end:
            f_pre_del = f_pre_del.next
            f_end = f_end.next
        f_pre_del.next = f_pre_del.next.next
        return dummy.next
