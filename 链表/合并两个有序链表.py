

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# 递归 
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
"""mergeTwoLists选择两个链表中的最小头节点连接"""
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val: #选择最小的头节点
            list1.next = self.mergeTwoLists(list1.next, list2)  #连接这一个最小的头节点和后一个最小的节点  
            return list1
        else:
            lsit2.next = self.mergeTwoLists(list2.next, list1)
            return list2
