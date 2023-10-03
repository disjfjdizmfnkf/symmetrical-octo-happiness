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

# 哈希表
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """用节点对象当键，而不是节点对象的值，值可能会有重复但不是循环的点，而节点对象只有一个"""
        hashMap ={}
        curNode = head
        while(curNode):
            if curNode in hashMap:
                return True
            hashMap[curNode] = 1
            curNode = curNode.next
        return False