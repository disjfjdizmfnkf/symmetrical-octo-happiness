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
var sortList = function (head) {
  if (head === null || head.next === null) return head;
  const mid = getMid(head);
  const r = mid.next;
  mid.next = null;

  const l1 = sortList(head);
  const l2 = sortList(r);
  return merge(l1, l2);
};

function getMid(head) {
  let s = head;
  let f = head;
  while (f && f.next) {
    s = s.next;
    f = f.next.next;
  }
  return s;
}

function merge(l1, l2) {
  const dummy = new ListNode();
  let cur = dummy;
  while (l1 && l2) {
    if (l1.val > l2.val) {
      cur.next = l2;
      l2 = l2.next;
    } else {
      cur.next = l1;
      l1 = l1.next;
    }
    cur = cur.next;
  }
  cur.next = l1 ? l1 : l2;
  return dummy.next;
}
