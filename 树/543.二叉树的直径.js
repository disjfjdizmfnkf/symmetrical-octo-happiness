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
 * @return {number}
 */
var diameterOfBinaryTree = function (root) {
  if (!root) return;
  let res = 0;
  function helper(node) {
    if (!node) return 0;
    const left = helper(node.left);
    const right = helper(node.right);
    res = Math.max(res, left + right + 1);
    return 1 + Math.max(left, right);
  }
  helper(root);
  return res - 1;
};
