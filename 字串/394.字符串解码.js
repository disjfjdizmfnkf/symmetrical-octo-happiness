/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function (s) {
  const stack = [];
  let curNum = 0;
  let curString = "";
  // NOTE: 四类字符对应四种情况 1.[ 字符开始 2.] 字符结束 3.数字 4.字母
  for (const char of s) {
    if (char === "[") {
      // 将curstring 腾出, 收集新字符, 并且将之前的收集到的数字加入栈中
      stack.push(curString);
      stack.push(curNum);
      curNum = 0;
      curString = "";
    } else if (char === "]") {
      // 这里收集字符完毕, 和之前的字符拼接起来即可
      const count = stack.pop();
      const prevString = stack.pop();
      curString = prevString + curString.repeat(count);
    } else if (isNumber) {
      // 修改curNum
      curNum = curNum * 10 + +char;
    } else {
      // 最后如果是字符修改curString
      curString += char;
    }
  }
  return curString;
}

const isNumber = (char) => /^[0-9]$/.test(char);
