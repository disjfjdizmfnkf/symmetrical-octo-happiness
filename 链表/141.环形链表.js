/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    const memo = new Set();
    while (head) {
        if (memo.has(head)) return true;
        memo.add(head);  //! 判断完将当前节点加入进去
        head = head.next;
    };
    return false;
};