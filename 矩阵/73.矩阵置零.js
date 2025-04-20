/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function (matrix) {
  const r = matrix.length;
  const c = matrix[0].length;
  const memo = new Set();
  for (let i = 0; i < r; i++) {
    for (let j = 0; j < c; j++) {
      if (matrix[i][j] === 0) {
        memo.add(`row-${i}`);
        memo.add(`col-${j}`);
      }
    }
  }

  for (let i = 0; i < r; i++) {
    for (let j = 0; j < c; j++) {
      if (memo.has(`row-${i}`) || memo.has(`col-${j}`)) {
        matrix[i][j] = 0;
      }
    }
  }
};
