/**
 * // Definition for a _Node.
 * function _Node(val,children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {_Node|null} root
 * @return {number[][]}
 */
var levelOrder = function (root) {
  if (!root) return [];
  const res = [];
  const queue = [];
  queue.push(root);
  while (queue.length) {
    const layer = [];
    const layerLen = queue.length;
    for (let i = 0; i < layerLen; i++) {
      const cur = queue.shift();
      if (cur.children.length) {
        for (const node of cur.children) {
          queue.push(node);
        }
      }
      layer.push(cur.val);
    }
    res.push(layer);
  }
  return res;
};
