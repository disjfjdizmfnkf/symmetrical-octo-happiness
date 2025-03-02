/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function (grid) {
  const rows = grid.length,
    cols = grid[0].length;
  let res = 0;
  let temp = 0;
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (grid[i][j] == 1) {
        bfs(i, j);
        res = Math.max(res, temp);
        temp = 0;
      }
    }
  }

  function bfs(row, col) {
    //! 递归超出最大深度的时候记得检查basecase是否正确
    //* 别忘记当前位置为0时也应该结束递归
    if (
      row < 0 ||
      row >= rows ||
      col < 0 ||
      col >= cols ||
      grid[row][col] === 0
    ) {
      return;
    }
    temp++;
    grid[row][col] = 0;
    bfs(row + 1, col);
    bfs(row - 1, col);
    bfs(row, col + 1);
    bfs(row, col - 1);
  }

  return res;
};
