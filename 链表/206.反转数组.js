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

//* 定义prev和cur参数
//* prev -> cur;   prev <- cur
var reverseList = function(head) {
    let temp;
    let cur = head, prev = null;
    while (cur) {
        temp = cur.next;
        cur.next = prev
        prev = cur;
        cur = temp;
    };
    return prev;
};