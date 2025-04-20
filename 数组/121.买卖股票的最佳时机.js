/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let low = prices[0];
  let res = 0;
  for (const p of prices) {
    if (p < low) {
      low = p;
    } else {
      res = Math.max(res, p - low);
    }
  }
  return res;
};
