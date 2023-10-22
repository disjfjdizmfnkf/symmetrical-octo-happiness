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