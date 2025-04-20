/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function (nums1, nums2) {
  const memo = new Map();
  const res = new Set();
  for (const num of nums1) {
    if (memo.has(num)) continue;
    else memo.set(num, 1);
  }
  for (const num of nums2) {
    if (memo.has(num)) {
      res.add(num);
    }
  }
  return Array.from(res);
};
