# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 使用dummy节点可以避免很多麻烦
class Solution1:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        cur, firstPart = head, dummy
        for i in range(left - 1):
            firstPart, cur = firstPart.next, cur.next

        # 完成逆序部分
        pre = None
        for i in range(right - left + 1):
            temp = cur.next  # temp 还有一个身份
            cur.next = pre
            pre = cur
            cur = temp
        firstPart.next.next = cur
        firstPart.next = pre

        return dummy.next
