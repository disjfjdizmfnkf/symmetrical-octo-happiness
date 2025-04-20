/**
 * @param {number[]} houses
 * @param {number[]} heaters
 * @return {number}
 */
var findRadius = function (houses, heaters) {
  let res = 0;
  heaters.sort((a, b) => a - b); //! 不传入参数等于按照字符串字典顺序
  for (const house of houses) {
    const i = _binarySearch(house, heaters);
    const a = Math.abs(heaters[i] - house);
    const b = i ? house - heaters[i - 1] : a + 1; // 如果i之前有元素
    res = Math.max(res, Math.min(a, b));
  }
  return res;
};

//！ 在合法范围内返回list中第一个大于target的元素索引 所以不一定返回的时大于target的数索引
function _binarySearch(target, list) {
  let l = 0,
    r = list.length - 1,
    m;
  while (l < r) {
    m = (l + r) >> 1;
    if (list[m] >= target) r = m;
    else l = m + 1;
  }
  return l; // 退出while循环的时候l和r指向同一个位置
}
