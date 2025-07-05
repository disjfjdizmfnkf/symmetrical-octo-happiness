/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function (n) {
  const solutions = [];
  const queens = new Array(n).fill(-1);  // NOTE : 表示对应row为索引的皇后位置
  // NOTE : C = R + b; C = - R + b;
  const columns = new Set();
  const diagonal1 = new Set();  // 主对角线: R - C
  const diagonal2 = new Set();  // 副对角线: R + C
  const row = new Array(n).fill(".");

  // NOTE : 根据当前皇后的位置生成棋盘
  function generateBoard() {
    const board = [];
    for (let i = 0; i < n; i++) {
      row[queens[i]] = "Q";
      board.push(row.join(""));
      row[queens[i]] = ".";
    }
    return board;
  }

  function backtrack(row) {
    if (row === n) {
      const board = generateBoard()
      solutions.push(board);
      return;
    }
    for (let i = 0; i < n; i++) {
      if (columns.has(i) || diagonal1.has(row - i) || diagonal2.has(row + i)) {
        continue;  // 剪枝: 如果当前列或对角线已被占用，则跳过
      }
      queens[row] = i;
      columns.add(i);
      diagonal1.add(row - i);
      diagonal2.add(row + i);
      backtrack(row + 1);
      diagonal2.delete(row + i);
      diagonal1.delete(row - i);
      columns.delete(i);
    }
  }

  backtrack(0);
  return solutions;
};
