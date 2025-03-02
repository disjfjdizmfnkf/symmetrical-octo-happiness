/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var reverseKGroup = function(head, k) {
    let dummy = new ListNode(0, head);
    let groupPrev = dummy;
    while (true) {
        let kth = getKth(groupPrev, k);
        if (!kth) break;

        // 反转k个链表
        let groupNext = kth.next;
        //! start: groupPrev.next | end: gtoupNext 
        let [newHead, newTail] = reverse(groupPrev.next, groupNext);
        // 连接
        groupPrev.next = newHead;
        newTail.next = groupNext;
        // 移动groupPrev为下一组准备
        groupPrev = newTail;
    }
    return dummy.next;
};

function getKth(node, k) {
    while (k > 0 && node) {
        k--;
        node = node.next;
    }
    return node;
}

//* reverse: 将cur指向prev
function reverse(start, end) {
    let prev = end;
    let cur = start;
    while (cur !== end) {  //! end不应该改变
        let temp = cur.next;
        cur.next = prev;
        prev = cur;
        cur = temp;
    }
    return [prev, start]
}
