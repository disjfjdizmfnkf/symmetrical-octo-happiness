/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function(text1, text2) {
    //* dp[i][j]: text1长度为i text2长度为j时的最长子序列长度
    const m = text1.length, n = text2.length;
    const dp = new Array(m + 1).fill(0).map(() => new Array(n + 1).fill(0));
    for (let i = 1; i <= m; i++) {
        const t1 = text1[i];
        for (let j = 1; j <= n; j++) {
            const t2 = text2[j];
            if (t1 === t2) {
                //! 我从哪里来: text1[i] === text2[j], dp[i][j] = dp[i - 1][j - 1] + 1 
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);  // 借助二维矩阵理解
            }
        }
    }
    return dp[m][n];
};