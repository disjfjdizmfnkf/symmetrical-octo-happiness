# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 两两一组交换
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 链表为空或者只有一个节点
        if not head or head.next:
            return head
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        # 当后面还有偶数个节点时
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next
            
            # 按结果从后往前
            # nxt = second.next
            # prev.next = second
            # second.next = first
            # first.next = nxt

            # 按结果从前往后
            first.next = second.next
            second.next = first
            prev.next = first
    
            # 将prev移动到下一组的前一个节点
            prev = first
