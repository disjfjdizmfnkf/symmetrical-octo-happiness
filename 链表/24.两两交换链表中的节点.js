/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function(head) {
    const dummy = new ListNode(0, head);
    let temp = dummy;
    // 反转链表，获取待反转链表的前一个节点，将后面的节点指向前面的节点
    while (temp.next && temp.next.next) {
        const node1 = temp.next;
        const node2 = temp.next.next;
        
        temp.next = node2;
        node1.next = node2.next;
        node2.next = node1;
        temp = node1;
    }
    return dummy.next;
};