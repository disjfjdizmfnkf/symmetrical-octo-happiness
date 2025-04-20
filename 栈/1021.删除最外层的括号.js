/**
 * @param {string} s
 * @return {string}
 */
var removeOuterParentheses = function (s) {
  let depth = 0; // 用于记录当前括号的嵌套深度
  let res = "";

  for (const char of s) {
    if (char === "(") {
      if (depth >= 1) res += char; //* 之前层级
      depth++; //* 当前层级
    } else {
      depth--; //* 先减少得到当前层级
      if (depth >= 1) res += char;
    }
  }
  return res;
};
