function heapSort(array) {
  //* 1.构建最大堆
  const n = arr.length;
  for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
    // 从最后一个非叶子节点开始
    heapify(arr, n, i);
  }

  // 从最后一个元素开始将最大值放在最后, 最后一个数可以不移动
  for (let i = n - 1; i > 0; i--) {
    [array[0], array[i]] = [array[i], array[0]];
    heapify(array, i, 0);
  }

  return array;
}

// 堆化操作(要排序的数组, 正在排序的数组长度, 当前调整的root索引)
function heapify(arr, len, rootIndex) {
  let max = rootIndex;
  const leftChild = 2 * rootIndex + 1;
  const rightChild = 2 * rootIndex + 2;

  // 找到左右节点中的最大值索引
  if (leftChild < len && arr[leftChild] > arr[max]) {
    max = leftChild;
  }
  if (rightChild < len && arr[rightChild] > arr[max]) {
    max = rightChild;
  }

  // 如果最大的不是根节点，交换并递归堆化
  if (max !== rootIndex) {
    [arr[rootIndex], arr[max]] = [arr[max], arr[rootIndex]];
    heapify(arr, len, max);
  }
}

// 示例用法
const array = [3, 6, 8, 10, 1, 2, 1];
console.log(heapSort(array)); // 输出: [1, 1, 2, 3, 6, 8, 10]
