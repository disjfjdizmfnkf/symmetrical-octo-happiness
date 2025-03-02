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
 * @return {number[][]}
 */
var levelOrder = function (root) {
  if (!root) return [];
  const queue = []; // 只是用来保存节点
  const res = [];
  queue.push(root);
  while (queue.length) {
    const layer = [];
    const layerLength = queue.length;
    for (let i = 0; i < layerLength; i++) {
      const node = queue.shift();
      layer.push(node.val);  //! 注意题目中定义的数据结构通过val获取值
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    res.push(layer);
  }
  return res;
};
