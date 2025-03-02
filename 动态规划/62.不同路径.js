/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function (m, n) {
  // 创建和初始化dp
  // const dp = new Array(m);
  // for (let i = 0; i < m; i++) {  //! 循环范围是m行
  //   dp[i] = new Array(n).fill(0);
  // }
  const dp = new Array(m).fill(0).map(()=> new Array(n).fill(0))
  dp[0][0] = 1;
  // 我从哪里来： dp[i][j] = dp[i - 1][j]  + dp[i][j - 1]
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      //! 一次判断加两个不好判断，可以一个判断加一个
      if (i > 0) dp[i][j] += dp[i - 1][j];
      if (j > 0) dp[i][j] += dp[i][j - 1];
    }
  }
  return dp[m - 1][n - 1];
};
