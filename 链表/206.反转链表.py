# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 准备三个指针，pre, cur, next ,
        # pre: 链表反转之后的最后一个节点,
        # cur: 未反转的链表的头节点，
        # next: cur之后的节点，为了改变cur的next指针之后不丢失这个节点
        pre, cur = None, head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    # 递归
    def reverseListRecursion(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        reversedTail, reversedHead = head.next, self.reverseList(head.next)
        # 将前面未反转的部分后面断开
        head.next = None
        # 将未反转部分接在反转后链表的尾巴后面
        reversedTail.next = head

        return reversedHead
