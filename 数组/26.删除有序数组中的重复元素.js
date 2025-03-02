/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  let i = 0;  //! i位置之前的数组是去重后的数组
  for (const num of nums) {
    if (i < 1 || num > nums[i - 1]) {  //* 和有序数组的最后一个元素比较
      nums[i] = num;
      i += 1;
    }
  }
  return i;
};
