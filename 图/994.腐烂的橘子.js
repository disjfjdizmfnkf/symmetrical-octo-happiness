  /**
   * @param {number[][]} grid
   * @return {number}
   */
  var orangesRotting = function (grid) {
    const R = grid.length, C = grid[0].length;
    const direction = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    const age = new Map();
    const queue = [];

    for (let r = 0; r < R; r++) {
      for (let c = 0; c < C; c++) {
        if (grid[r][c] === 2) {
          const code = r * C + c;
          queue.push(code);
          age.set(code, 0); //NOTE: 初始化时间为0
        }
      }
    }

    let res = 0;
    while (queue.length) {
      const code = queue.shift();
      const r = Math.floor(code / C), c = Math.floor(code % C);
      for (const d of direction) {
        const nr = r + d[0];
        const nc = c + d[1];

        if (nr >= 0 && nr < R && nc >= 0 && nc < C && grid[nr][nc] === 1) {
          grid[nr][nc] = 2;
          const ncode = nr * C + nc;
          queue.push(ncode);
          age.set(ncode, age.get(code) + 1);
          res = age.get(ncode);
        }
      }
    }

    const fresh = grid.reduce((acc, row) => acc + row.reduce((acc, cur) => acc + (cur === 1 ? 1 : 0), 0), 0)
    return fresh > 0 ? -1 : res;
  }
