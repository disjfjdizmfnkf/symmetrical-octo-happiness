/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function (head) {
  const midNode = getMidNode(head);
  let head2 = midNode.next;
  midNode.next = null;
  head2 = reverseList(head2);
  while (head2) {  //! head要么和head一样长要么更短,这是由getMidNode函数决定的
    //* 保存两个指针的下一个节点
    const nxt = head.next;
    const nxt2 = head2.next;
    head.next = head2;
    head2.next = nxt;

    head = nxt;
    head2 = nxt2;
  }
};

//! 这种方法返回中间或中间左侧节点
function getMidNode(head) {
  let slow = head, fast = head.next;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }
  return slow;
}

function reverseList(head) {
  let cur = head, prev = null, temp;
  while (cur) {
    temp = cur.next;
    cur.next = prev;
    prev = cur;
    cur = temp;
  }
  return prev;
}
