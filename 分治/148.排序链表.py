# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        mid = self.get_mid(head)
        l, r = head, mid.next
        mid.next = None

        left = self.sortList(l)
        right = self.sortList(r)

        return self.merge(left, right)

    def get_mid(self, head):  # 使用双指针寻找中间节点
        slow, fast = head, head.next  # 还是不知道为什么不能都从head开始
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow

    def merge(self, head1, head2):
        dummy = tail = ListNode()
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        tail.next = head1 if head1 else head2
        return dummy.next


