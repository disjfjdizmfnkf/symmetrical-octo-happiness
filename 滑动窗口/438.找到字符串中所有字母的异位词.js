/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
//NOTE: 字串是异位词 (窗口中的相同字母数量相同)
var findAnagrams = function (s, p) {
  const res = [];
  const pLen = p.length;
  const sLen = s.length;
  if (pLen > sLen) return res;
  //NOTE: 使用数组代替对象，索引为字符的ASCII码  a: 97
  const pCount = new Array(26).fill(0);  //NOTE : 统计26个字母数量
  const windowCount = new Array(26).fill(0);
  // 统计
  for (let i = 0; i < pLen; i++) {
    pCount[p.charCodeAt(i) - 97]++;
  }
  // 初始化滑动窗口
  for (let i = 0; i < pLen; i++) {
    windowCount[s.charCodeAt(i) - 97]++;
  }
  // 首次需要检查
  if (arraysEqual(windowCount, pCount)) {
    res.push(0);
  }
  // 调整窗口边界
  for (let r = pLen; r < sLen; r++) {
    windowCount[s.charCodeAt(r - pLen) - 97]--;  // 左边界
    windowCount[s.charCodeAt(r) - 97]++;  // 右边界
    // 判断
    if (arraysEqual(windowCount, pCount)) {
      res.push(r - pLen + 1);
    }
  }
  return res;
};


function arraysEqual(arr1, arr2) {
  for (let i = 0; i < 26; i++) {
    if (arr1[i] !== arr2[i]) return false;
  }
  return true;
}
