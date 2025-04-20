/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function (nums) {
  if (nums.length <= 0) return;
  const mid = ~~(nums.length / 2);
  const root = nums[mid];
  const left = sortedArrayToBST(nums.slice(0, mid));
  const right = sortedArrayToBST(nums.slice(mid + 1));
  return new TreeNode(root, left, right);
};
