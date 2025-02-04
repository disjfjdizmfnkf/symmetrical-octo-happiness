# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            Kth = self.getKth(groupPrev, k)
            if not Kth:
                break
            groupNext = Kth.next

            # 反转节点并获取反转后的首尾节点
            newHead, newTail = self.reverse(groupPrev.next, groupNext)
            # 重新链接反转后的链表部分
            groupPrev.next = newHead
            newTail.next = groupNext
            # 更新groupPrev到下一个节点的位置
            groupPrev = newTail

        return dummy.next

    def getKth(self, node: ListNode, k: int) -> ListNode:
        while node and k:
            node = node.next
            k -= 1
        return node

    def reverse(self, start: ListNode, end: ListNode) -> (ListNode, ListNode):
        prev, cur = end, start
        while cur != end:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev, start


