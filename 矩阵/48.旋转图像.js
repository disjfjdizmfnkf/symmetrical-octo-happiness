/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function (matrix) {
  const n = matrix.length;
  const queue = [];
  // 将元素按行顺序存入队列
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      queue.push(matrix[i][j]);
    }
  }
  // 从最后一列到第一列
  for (let col = n - 1; col >= 0; col--) {
    for (let row = 0; row < n; row++) {
      matrix[row][col] = queue.shift();
    }
  }
};
