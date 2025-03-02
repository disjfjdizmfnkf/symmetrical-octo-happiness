/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    const dummy = new ListNode(0, head);
    let cur = dummy, p = dummy;
    //! 获取删除节点的前后节点
    let before = new ListNode(0, dummy), after = cur.next;
    while (n) {
        p = p.next;
        n--;
    }
    while (p) {
        //* 让这些节点保持一定距离一起往后走
        before = before.next;
        cur = cur.next;
        after = after.next;
        p = p.next;
    }

    before.next = after;
    cur.next = null;
    return dummy.next;
};


//? 剑指offer 22 获取倒数第k个节点
var _removeNthFromEnd = function(head, n) {
    const dummy = new ListNode(0, head);
    let cur = dummy, p = dummy;
    while (n) {
        p = p.next;
        n--;
    }
    while (p) {
        cur = cur.next;
        p = p.next;
    }
    return cur.val;
};