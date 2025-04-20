/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function (s) {
  let res = 0;
  const stack = [-1]; //* 保存当前有效括号开始的左括号索引

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(") {
      stack.push(i);
    } else {
      stack.pop();
      if (stack.length === 0) {
        stack.push(i);
      } else {
        res = Math.max(res, i - stack[stack.length - 1]);
      }
    }
  }

  return res;
};
