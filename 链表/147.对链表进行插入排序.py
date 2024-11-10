# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre, cur = head, head.next

        while cur:
            # 跳过满足从小到大排序的部分
            if cur.val >= pre.val:
                pre, cur = cur, cur.next
                continue
            # 后面的节点小于cur 需要插入到正确位置
            # 错误代码，想想为什么
            # temp = dummy.next
            # while cur.val > temp.val:
            temp = dummy
            while cur.val > temp.next.val:   # 想像temp带着cur一起走
                temp = temp.next
            # 结束while时 cur.val < temp.val 插入到前面
            pre.next = cur.next
            cur.next = temp.next
            temp.next = cur
            cur = pre.next
        return dummy.next