/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function (word1, word2) {
    const dp = new Array(word1.length + 1).fill(0).map(() => new Array(word2.length + 1).fill(0));
    //* 初始化
    for (let i = 1; i <= word1.length; i++) dp[i][0] = i;
    for (let j = 1; j <= word2.length; j++) dp[0][j] = j;
    //* 应用递推公式
    for (let i = 1; i <= word1.length; i++) {
      for (let j = 1; j <= word2.length; j++) {
        if (word1[i - 1] === word2[j - 1]) {
          dp[i][j] = dp[i - 1][j - 1];
        } else {
          //* 插入: 如果插入可以解决dp[j] 那么考虑dp[i][j - 1]
          //* 删除: 如果删除[i]可以解决dp[j] 考虑dp[i - 1][j]
          //* 交换: dp[i-1][j-1]
          dp[i][j] = Math.min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1;
        }
      }
    }
    return dp[word1.length][word2.length];
  };
  