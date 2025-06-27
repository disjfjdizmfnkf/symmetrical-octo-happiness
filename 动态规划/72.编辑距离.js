/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function (word1, word2) {
  // NOTE: dp 表示word1长度为i word1长度为j时的最小修改次数
  const dp = new Array(word1.length + 1).fill(0).map(() => new Array(word2.length + 1).fill(0));

  // NOTE:初始化  两个中只有一个有长度时的修改次数
  for (let i = 1; i <= word1.length; i++) dp[i][0] = i;
  for (let j = 1; j <= word2.length; j++) dp[0][j] = j;

  for (let i = 1; i <= word1.length; i++) {
    for (let j = 1; j <= word2.length; j++) {
      // case1: the last character of word1 and word2 is same
      if (word1[i - 1] === word2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1];
      } else {
        // case2: need inset or delete or exchange
        //* 插入: 如果插入可以解决dp[j] 那么修改次数取决于dp[i][j - 1]
        //* 删除: 如果删除[i]可以解决dp[j] 修改次数取决于dp[i - 1][j]
        //* 交换: dp[i-1][j-1]
        dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1;
      }
    }
  }
  return dp[word1.length][word2.length];
};
