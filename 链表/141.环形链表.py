# 双指针 floyd循环检测算法 龟兔赛跑算法
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_pointer = head
        fast_pointer = head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False

# 利用不同节点对象的不同(不是值的不同)


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """使用节点自身当key是独一无二的"""
        memo = set()
        while (head):
            if head in memo:
                return True
            memo.add(head)
            head = curNode.next
        return False
