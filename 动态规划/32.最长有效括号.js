/**
 * @param {string} s
 * @return {number}
 */
function longestValidParentheses(s) {
  const n = s.length;
  if (n < 2) return 0;
  const dp = new Array(n).fill(0);
  let maxVal = 0;

  for (let i = 1; i < n; i++) {
    if (s[i] === ')') {
      if (s[i - 1] === '(') {
        dp[i] = (i >= 2 ? dp[i - 2] : 0) + 2;
      } else if (i - dp[i - 1] - 1 >= 0 && s[i - dp[i - 1] - 1] === '(') {
        dp[i] = dp[i - 1] + 2 + (i - dp[i - 1] - 2 >= 0 ? dp[i - dp[i - 1] - 2] : 0);
      }
      maxVal = Math.max(maxVal, dp[i]);
    }
  }
  return maxVal;
}
