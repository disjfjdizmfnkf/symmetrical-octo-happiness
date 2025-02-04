var restoreIpAddresses = function (s) {
  const res = [];
  const n = s.length;

  // 0.0.0.0 - 255.255.255.255
  if (n < 4 || n > 12) return res;

  function backtrack(combine, start = 0) {
    // 如果当前已经有四段了
    if (combine.length === 4) {
      if (start === n) {
        res.push(combine.join("."));
      }
      return;
    }
    for (let i = 1; i <= 3; i++) {
      const sub = s.substring(start, start + i);
      // 1.差分的结果中不能有前导0 2.作为数字的结果不能>255
      if (sub.length > 1 && sub[0] === "0") continue;
      if (+sub > 255) continue;
      backtrack([...combine, sub], start + i);
    }
  }

  backtrack([]);
  return res;
};
