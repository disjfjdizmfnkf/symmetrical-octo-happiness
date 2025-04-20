/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function (coins, amount) {
  const dp = new Array(amount + 1).fill(amount + 1);
  dp[0] = 0;  //! dp[0] 是可达的, 一定要初始化
  //! dp[i] 金额为i的最小硬币数量
  for (let i = 1; i <= amount; i++) {
    for (const coin of coins) {
      if (i >= coin) {
        dp[i] = Math.min(dp[i], dp[i - coin] + 1);  //! 硬币数量加一
      }
    }
  }
  return dp[amount] > amount ? -1 : dp[amount];
};
