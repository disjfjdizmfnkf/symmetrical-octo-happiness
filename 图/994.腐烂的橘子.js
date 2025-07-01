/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function (grid) {
  let rows = grid.length, cols = grid[0].length;
  let directions = [[-1, 0], [0, -1], [1, 0], [0, 1]];
  let queue = [];  // 存放腐烂橘子坐标
  let depth = new Map();  // 存放每个橘子腐烂的时间

  for (let r = 0; r < R; ++r) {
    for (let c = 0; c < C; ++c) {
      if (grid[r][c] === 2) {
        const code = r * C + c;
        queue.push(code);
        depth.set(code, 0);
      }
    }
  }

  const ans = 0;
  while (queue.length > 0) {
    let code = queue.shift();
    let r = Math.floor(code / cols), c = code % cols;
    for (let d of directions) {
      let nr = r + d[0], nc = c + d[1];
      if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] === 1) {
        grid[nr][nc] = 2;
        let newCode = nr * cols + nc;
        queue.push(newCode);
        depth.set(newCode, depth.get(code) + 1);
        ans = depth.get(newCode);
      }

    }

    const fresh = grid.reduce((acc, row) => acc + row.reduce((acc, cur) => acc + (cur === 1 ? 1 : 0), 0), 0)
    return fresh > 0 ? -1 : res;
  }

  const refreshCount = grid.reduce((acc, row) => acc + row.reduce((acc, v) => acc + (v === 1 ? 1 : 0), 0), 0);
  return refreshCount > 0 ? -1 : ans;
}
