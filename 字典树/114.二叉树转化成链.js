/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {void} Do not return anything, modify root in-place instead.
 */
// react fiber架构采用这种思想拆分渲染任务
var flatten = function (root) {
  // 按照先序将root展开
  let cur = root;
  while (cur) {
    if (cur.left) {
      let pre = cur.left;
      while (pre.right) pre = pre.right;  // 找到左子树的最右节点（前驱）
      // 将原右子树接到前驱的右侧
      pre.right = cur.right;
      // 把左子树整体移到右边，并置空左指针
      cur.right = cur.left;
      cur.left = null;
    }
    cur = cur.right;  // 继续处理下一个节点（先序展开后的右链）
  }
};

function flatten(root) {
  let prev = null;
  function dfs(node) {
    if (!node) return;
    dfs(node.right);
    dfs(node.left);
    node.right = prev;  //! 逆序的前一个也就是正序下一个
    node.left = null;
    prev = node;
  }
  dfs(root);
}
// 多叉树
function flatten(root) {
  let prev = null;
  function dfs(node) {
    if (!node) return;
    // 逆序遍历所有子节点
    for (let i = node.children.length - 1; i >= 0; i--) {
      dfs(node.children[i]);
    }
    // 将当前节点的所有子节点展平为链表
    node.right = prev;  //! 逆序的前一个也就是正序下一个
    node.children = []; // 清空多叉树的子节点
    prev = node;
  }
  dfs(root);
}