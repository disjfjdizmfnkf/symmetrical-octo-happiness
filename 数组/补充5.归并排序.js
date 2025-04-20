/**
 * 归并排序
 * @param {number[]} array 待排序的数组
 * @return {number[]} 排序后的数组
 */
function mergeSort(array) {
  if (array.length <= 1) return array;

  const middle = Math.floor(array.length / 2);
  const left = array.slice(0, middle);
  const right = array.slice(middle);

  return merge(mergeSort(left), mergeSort(right));
}

/**
 * 合并两个有序数组
 * @param {number[]} left 左侧有序数组
 * @param {number[]} right 右侧有序数组
 * @return {number[]} 合并后的有序数组
 */
function merge(left, right) {
  let result = [];
  let leftIndex = 0;
  let rightIndex = 0;

  while (leftIndex < left.length && rightIndex < right.length) {
    if (left[leftIndex] < right[rightIndex]) {
      result.push(left[leftIndex]);
      leftIndex++;
    } else {
      result.push(right[rightIndex]);
      rightIndex++;
    }
  }

  // 合并剩余的元素
  return result.concat(left.slice(leftIndex)).concat(right.slice(rightIndex));
}

// 示例用法
const array = [38, 27, 43, 3, 9, 82, 10];
const sortedArray = mergeSort(array);
console.log(sortedArray); // 输出: [3, 9, 10, 27, 38, 43, 82]
