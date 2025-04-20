/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function (root, p, q) {
  if (!root) return;
  //! 为什么返回的是root? 如果两个节点都在一边, p, q都会返回自身,而root收到的return就是最靠近root的节点也就是祖先
  if (root === p || root === q) return root;
  //! 写糊涂了，忘了是在子树上递归
  const left = lowestCommonAncestor(root.left, p, q);
  const right = lowestCommonAncestor(root.right, p, q);
  return left && right ? root : (left || right);
};
