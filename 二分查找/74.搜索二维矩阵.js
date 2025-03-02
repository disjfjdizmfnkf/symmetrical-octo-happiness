/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
//! 在判断目标在哪一行的时候需要和mid行首位元素比较
var searchMatrix = function (matrix, target) {
  const rows = matrix.length,
    cols = matrix[0].length;
  let targetRow = -1;

  let top = 0,
    bottom = rows - 1;
  while (top <= bottom) {
    const mid = Math.floor((top + bottom) / 2);
    if (target > matrix[mid][cols - 1]) {
      top = mid + 1;
    } else if (target < matrix[mid][0]) {
      bottom = mid - 1;
    } else {
      targetRow = mid;
      break;
    }
  }

  if (targetRow === -1) return false;

  let l = 0,
    r = cols - 1;
  while (l <= r) {
    const mid = Math.floor((l + r) / 2);
    if (target > matrix[targetRow][mid]) {
      l = mid + 1;
    } else if (target < matrix[targetRow][mid]) {
      r = mid - 1;
    } else {
      return true;
    }
  }
  return false;
};
