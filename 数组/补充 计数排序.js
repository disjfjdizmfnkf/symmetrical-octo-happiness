//* 计数排序
//! 只对于非负数有用
function countSort(array) {
    const min = Math.min(...array), max = Math.max(...array);
    const countNum = new Array(max - min + 1).fill(0);
    for (const item of array) {
      countNum[item - min] += 1;
    }
  
    let i = 0; // 指向array开始的位置
    for (let j = 0; j < countNum.length; j++) {
      while (countNum[j] > 0) {
        array[i] = j + min;  //! 记得加上作为base的min
        countNum[j]--;
        i++;
      }
    }
    return array;
  }
  const array = [3, 6, 8, 10, 1, 2, 1];
  console.log(countSort(array)); // 输出: [1, 1, 2, 3, 6, 8, 10]
  