/**
 * @param {string} num
 * @param {number} k
 * @return {string}
 */
var removeKdigits = function (num, k) {
  const stack = [];
  for (const n of num) {
    // 当栈顶元素大于当前数字且仍需移除数字时，移除栈顶元素
    while (stack.length && k > 0 && n < stack[stack.length - 1]) {
      stack.pop();
      k--;
    }
    // 如果是前导0直接不添加了
    if (!(stack.length === 0 && n === "0")) stack.push(n);
  }
  // 如果还有剩余的 k，移除栈顶的 k 个元素
  stack.splice(stack.length - k, k);
  return stack.length ? stack.join("") : "0";
};
