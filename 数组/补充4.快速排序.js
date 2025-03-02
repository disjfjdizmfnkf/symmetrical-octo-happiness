function quickSort(list) {
  if (list.length <= 1) return list;

  const randIndex = Math.floor(Math.random() * list.length);
  const pivot = list[randIndex];
  const left = [];
  const right = [];

  for (let i = 0; i < list.length; i++) {
    if (i === randIndex) continue;
    if (list[i] > pivot) {
      right.push(list[i]);
    } else {
      left.push(list[i]);
    }
  }

  return [...quickSort(left), pivot, ...quickSort(right)];
} // 示例用法
const array = [3, 6, 8, 10, 1, 2, 1];
console.log(quickSort(array)); // 输出: [1, 1, 2, 3, 6, 8, 10]
