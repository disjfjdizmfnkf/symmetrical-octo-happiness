# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=23, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(23, head)
        groupPrev = dummy
        while True:
            # 在这个循环过程中相关的变量都是之后会不断调整值的变量
            Kth = self.getKth(groupPrev, k)
            if not Kth:
                break

            # 如果之后有k个节点,反转之后的节点
            # 反转节点时需要拿到开始节点和前一个节点
            # 在这里因为最后一个节点不是空节点，所以还要获取下一组的第一个节点
            cur, prev = groupPrev.next, Kth.next
            groupNext = Kth.next
            while cur != groupNext:
                temp = cur.next
                cur.next = prev
                # 将两个指针向后移动
                prev = cur
                cur = temp
            # groupPrev的next重新链接，并且修改groupPrev到下一个节点的位置
            temp = groupPrev.next
            groupPrev.next = Kth
            groupPrev = temp
        return dummy.next

    def getKth(self, node, k):
        while node and k:
            node = node.next
            k -= 1
        return node


