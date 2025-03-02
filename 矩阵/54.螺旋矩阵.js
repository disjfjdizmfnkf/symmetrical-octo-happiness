/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
  let top = 0,
    left = 0,
    bottom = matrix.length - 1,
    right = matrix[0].length - 1;
  const res = [];
  while (1) {
    // left => right
    for (let i = left; i <= right; i++) {
      res.push(matrix[top][i]);
    }
    top++;
    if (top > bottom) break;
    // top => bottom
    for (let i = top; i <= bottom; i++) {
      res.push(matrix[i][right]);
    }
    right--;
    if (right < left) break;
    // right => left
    for (let i = right; i >= left; i--) {
      res.push(matrix[bottom][i]);
    }
    bottom--;
    if (bottom < top) break;
    // bottom => top
    for (let i = bottom; i >= top; i--) {
      res.push(matrix[left][i]);
    }
    left++;
    if (left > right) break;
  }
  return res;
};

