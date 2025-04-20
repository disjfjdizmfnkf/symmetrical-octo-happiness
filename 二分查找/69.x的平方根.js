/**
 * @param {number} x
 * @return {number}
 */
//* 有m * m 决定目标的区间
var mySqrt = function(x) {
    let res = -1;
    let l = 0, r = x, m;
    while (l <= r) {
      m = (l + r) >> 1;
      if (m * m <= x) {
        res = m;
        l = m + 1;
      } else {
        r = m - 1;
      }
    }
    return res;
  };