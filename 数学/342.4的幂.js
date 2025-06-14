
/**
 * @param {number} n
 * @return {boolean}
 */
// 使用递归
var isPowerOfFour = function (n) {
  if (n === 4 || n === 1) return true;
  if (isFloat(n) || n < 4) return false;
  return isPowerOfFour(n / 4);
};

function isFloat(n) {
  return typeof n === 'number' && !Number.isNaN(n) && !Number.isInteger(n);
}

