/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
/* 
k表示是第k大的数
k = 4; k / 2 = 2;比较2,5 2 < 5 移除 1 2
list1: 1 2 3 
list2: 4 5

k = 2; k / 2 = 1;比较3,4 3 < 4 移除 3
list1: 3
list2: 4 5

k = 1; 
第1大的数字是4
list1: 
list2: 4 5
*/
var findMedianSortedArrays = function (nums1, nums2) {
  const total = nums1.length + nums2.length;
  if (total % 2 === 1) {
    return findKth(nums1, 0, nums2, 0, (total + 1) >> 1);
  } else {
    const left = findKth(nums1, 0, nums2, 0, total >> 1);
    const right = findKth(nums1, 0, nums2, 0, (total >> 1) + 1);
    return (left + right) / 2;
  }
};

const findKth = function (nums1, start1, nums2, start2, k) {
  const len1 = nums1.length - start1, len2 = nums2.length - start2;
  // 确保nums1是较短的数组，方便处理
  if (len1 > len2) return findKth(nums2, start2, nums1, start1, k);
  // nums1为空的情况
  if (len1 === 0) return nums2[start2 + k - 1];
  // k为1时，直接返回较小的元素
  if (k === 1) return Math.min(nums1[start1], nums2[start2]);
  // 确定比较的位置 p需要判断短数组的长度够不够
  const p = Math.min(k >> 1, len1), q = k >> 1;
  const idx1 = start1 + p - 1, idx2 = start2 + q - 1;
  // 递归排除元素
  if (nums1[idx1] < nums2[idx2]) {
    return findKth(nums1, start1 + p, nums2, start2, k - p);
  } else {
    return findKth(nums1, start1, nums2, start2 + q, k - q);
  }
};
