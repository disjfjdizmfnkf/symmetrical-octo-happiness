// https://pic.leetcode-cn.com/171cad48cd0c14f565f2a0e5aa5ccb130e4562906ee10a84289f12e4460fe164-image.png
/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var multiply = function (num1, num2) {
  if (num1 === "0" || num2 === "0") return "0";
  const res = new Array(num1.length + num2.length).fill(0);
  //! 从后往前 从低位到高位计算
  for (let i = num1.length - 1; i >= 0; i--) {
    const n1 = +num1[i];
    for (let j = num2.length - 1; j >= 0; j--) {
      const n2 = +num2[j];
      // len1 + len2 - 1 = index
      // (i+1) + (j+1) - 1 = index
      const sum = res[i + j + 1] + n1 * n2;  
      res[i + j + 1] = sum % 10;
      res[i + j] += Math.floor(sum / 10);  //! 加上进位
    }
  }

  let result = "";
  for (let i = 0; i < res.length; i++) {
    if (i === 0 && res[i] === 0) continue;  //! 判断第一个位置是否有进位
    result = result + res[i];
  }
  return result;
};
