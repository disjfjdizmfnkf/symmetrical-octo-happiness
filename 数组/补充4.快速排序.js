/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function (nums, start = 0, end = nums.length - 1) {
  if (start < end) {
    const pivot = partition(nums, start, end);
    sortArray(nums, start, pivot - 1);
    sortArray(nums, pivot + 1, end);
  }
  return nums;
};

function partition(nums, start, end) {
  // const randIdx = Math.floor(Math.random() * (end - start + 1)) + start;
  // [nums[randIdx], nums[start]] = [nums[start], nums[randIdx]];
  const pivot = start;
  let i = start;
  //! 这里将pivot放在start, 所以从start + 1开始
  for (let j = start + 1; j <= end; j++) {
    if (nums[j] <= nums[pivot]) {
      i++;
      [nums[j], nums[i]] = [nums[i], nums[j]];
    }
  }
  [nums[pivot], nums[i]] = [nums[i], nums[pivot]];
  return i;
}



/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function (nums) {
  if (nums.length <= 1) return nums;
  quickSort(nums, 0, nums.length - 1);
  return nums;
};

function quickSort(arr, left, right) {
  if (left >= right) return;

  // 随机选择轴点并交换到最左端
  const randIndex = Math.floor(Math.random() * (right - left + 1)) + left;
  [arr[left], arr[randIndex]] = [arr[randIndex], arr[left]];
  const pivot = arr[left];

  let lt = left; // 小于pivot的右边界
  let gt = right; // 大于pivot的左边界
  let i = left + 1; // 当前元素

  while (i <= gt) {
    if (arr[i] < pivot) {
      [arr[i], arr[lt]] = [arr[lt], arr[i]];
      lt++;
      i++;
    } else if (arr[i] > pivot) {
      [arr[i], arr[gt]] = [arr[gt], arr[i]];
      gt--;
    } else {
      i++;
    }
  }

  // 递归排序小于和大于的部分
  quickSort(arr, left, lt - 1);
  quickSort(arr, gt + 1, right);
}


