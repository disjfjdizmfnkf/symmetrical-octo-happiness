/**
 * @param {number} n
 * @return {string}
 */
var thousandSeparator = function (n) {
  //! 两个量词不能放在一起
  return String(n).replace(/(\d)(?=(\d{3})+$)/g, "$1" + ".");
};

var thousandSeparator2 = function (n) {
    return n.toLocaleString();
  };
  

var thousandSeparator3 = function (n) {
  let str = String(n);
  let result = "";
  let count = 0;

  for (let i = str.length - 1; i >= 0; i--) {
    result = str[i] + result;
    count++;
    if (count % 3 === 0 && i !== 0) {
      result = "." + result;
    }
  }

  return result;
}

console.log(thousandSeparator2(123456789)); // 输出: "123.456.789"
