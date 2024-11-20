# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
        temp = self.gitMid(head)  # 返回以head为头的链的中间节点或者左边的
        right = temp.next
        temp.next = None  # 从中间断开

        left, right = self.sortList(left), self.sortList(right)
        return self.merge(left, right)

    def gitMid(self, head):  # 使用双指针寻找中间节点
        slow, fast = head, head.next  # fast为head.next 时在偶数长度的链表中可以均匀分隔
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # 注意这里的参数需要传入self
    def merge(self, l1, l2):
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next
