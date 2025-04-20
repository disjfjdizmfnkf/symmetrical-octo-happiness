/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function (s) {
  const stack = [], curNum = 0, curString = "";
  for (const char of s) {
    if (c === "[") {
      stack.push(curString);
      stack.push(curNum);
      curString = "";
      curNum = 0;
    } else if (c === "]") {
      const num = stack.pop();
      const prevString = stack.pop();
      curString = prevString + curString.repeat(num);
    } else if (!isNaN(c)) {
      curNum = curNum * 10 + +c;
    } else {
      curString = c + curString;
    }
  }
  return curString;
};
