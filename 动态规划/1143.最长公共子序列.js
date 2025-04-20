/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
//* dp[i][j]: text1长度为i text2长度为j时的最长子序列长度
var longestCommonSubsequence = function (text1, text2) {
    let len1 = text1.length, len2 = text2.length;
    const dp = new Array(len1 + 1).fill(0).map(() => new Array(len2 + 1).fill(0));
    for (let i = 1; i <= len1; i++) {
      const char1 = text1[i - 1];
      for (let j = 1; j <= len2; j++) {
        const char2 = text2[j - 1];
        if (char1 === char2) dp[i][j] = dp[i - 1][j - 1] + 1;
        else dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
      }
    }
    return dp[len1][len2];
  };
  