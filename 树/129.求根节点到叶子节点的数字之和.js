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
var sumNumbers = function(root) {
    let res = 0;
    function bfs(root, sum) {
        if(!root) {
            return;
        }
        if (!root.left && !root.right) {
            res += sum * 10 + root.val;
        }
        bfs(root.left, sum * 10 + root.val);
        bfs(root.right, sum * 10 + root.val);
    }
    bfs(root, 0);
    return res;
};