/**
 * @param {number} n
 * @return {number}
 */
var fib = function (n) {
  if (n < 2) return n;
  let a = 0, b = 1, c;
  for (let i = 2; i <= n; i++) {
    c = a + b;
    a = b;
    b = c;
  }
  return c;
};
