# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        left = head
        right = self.gitMid(head)  # 返回以head为头的链的中间节点或者左边的
        temp = right.next
        right.next = None  # 从中间断开
        right = temp

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)

    def gitMid(self, head):  # 使用双指针寻找中间节点
        slow, fast = head, head.next         # 所以为什么开始不能给fast赋值head？？？？？？？？？？
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        dummy = tail = ListNode()
        while left and right:
            if left.val > right.val:
                tail.next = right
                right = right.next
            else:
                tail.next = left
                left = left.next
            tail = tail.next
        if left:
            tail.next = left
        if right:  # 不使用else因为left right 可以同时为0
            tail.next = right
        return dummy.next


# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head
#         mid = self.get_mid(head)
#         l, r = head, mid.next
#         mid.next = None
#
#         left = self.sortList(l)
#         right = self.sortList(r)
#
#         return self.merge(left, right)
#
#     def get_mid(self, head):
#         slow, fast = head, head.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         return slow
#
#     def merge(self, head1, head2):
#         dummy = tail = ListNode()
#         while head1 and head2:
#             if head1.val < head2.val:
#                 tail.next = head1
#                 head1 = head1.next
#             else:
#                 tail.next = head2
#                 head2 = head2.next
#             tail = tail.next
#
#         tail.next = head1 if head1 else head2
#
#         return dummy.next