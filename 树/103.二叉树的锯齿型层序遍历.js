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
 * @return {number[][]}  // NOTE: 数字
 */
var zigzagLevelOrder = function (root) {
  if (!root) return []; //! 记得处理特殊情况
  const queue = [];
  const res = [];
  queue.push(root);
  let isLeftToRight = true; //! flag声明在遍历外层
  while (queue.length) {
    const layerLen = queue.length;
    const layer = [];
    for (let i = 0; i < layerLen; i++) {
      const node = queue.shift(); //! 这里是先进先出
      // 添加当前节点子节点
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
      // 通过遍历方向确定是前加还是后加
      if (isLeftToRight) {
        layer.push(node.val); //NOTE: 注意返回值要求
      } else {
        layer.unshift(node.val);
      }
    }
    isLeftToRight = !isLeftToRight; //! 每一层结束之后改变遍历方向
    res.push(layer);
  }
  return res;
};

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
var zigzagLevelOrder = function (root) {
  // 处理根节点为空的情况
  if (!root) return [];

  const queue = [];
  const res = [];
  queue.push(root);
  let isLeftToRight = true;

  while (queue.length) {
    const layerLen = queue.length;
    const layer = [];

    for (let i = 0; i < layerLen; i++) {
      // 从队列头部取出元素
      const node = queue.shift();

      // 添加当前节点子节点
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);

      // 根据遍历方向记录节点值
      if (isLeftToRight) {
        layer.push(node.val);
      } else {
        layer.unshift(node.val);
      }
    }

    // 每一层结束后改变遍历方向
    isLeftToRight = !isLeftToRight;
    res.push(layer);
  }

  return res;
};
