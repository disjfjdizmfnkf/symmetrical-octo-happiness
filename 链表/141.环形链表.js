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
//* time: O(1)
var hasCycle = function(head) {
    let s = head, f = head;
    while(f && f.next) {
        s = s.next;
        f = f.next.next;
        if (s === f) return true;
    }
    return false;
};

//* 通解
var hasCycle = function(head) {
    const memo = new Set();
    while (head) {
        if (memo.has(head)) return true;
        memo.add(head);  //! 判断完将当前节点加入进去
        head = head.next;
    };
    return false;
};