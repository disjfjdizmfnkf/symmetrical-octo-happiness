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
var deleteDuplicates = function (head) {
    const dummy = new ListNode(0, head);
    let cur = dummy;
    while (cur.next && cur.next.next) {
      const val = cur.next.val;
      // * 判断后面是否有重复元素
      if (cur.next.next.val === val) {
        //* 如果有重复元素, 从第一个开始判断删除
        while (cur.next && cur.next.val === val) {
          cur.next = cur.next.next;
        }
      } else {
        //! 每轮判断没有重复元素才向后移动
        cur = cur.next;
      }
    }
    return dummy.next;
  };
  