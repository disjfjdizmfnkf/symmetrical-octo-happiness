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
 * @return {boolean}
 */
var isSymmetric = function (root) {
  if (!root) return;
  function helper(left, right) {
    if (!left || !right) return left === right;
    return (
      left.val === right.val &&
      helper(left.left, right.right) &&
      helper(left.right, right.left)
    );
  }
  return helper(root.left, root.right);
};
