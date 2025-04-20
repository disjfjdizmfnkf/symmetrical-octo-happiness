/**
 * @param {string} path
 * @return {string}
 */
//* 使用split
var simplifyPath = function (path) {
  const token = path.split("/");
  const stack = [];
  for (const p of token) {
    if (p === "." || p === "") continue;
    else if (p === "..") {
      //! 这里只是一共子情况 如果写 p === ".." && stack.length 和其它情况就不互斥了
      if (stack.length) {
        stack.pop();
      }
    } else {
      stack.push(p);
    }
  }
  return "/" + stack.join("/");
};

//* 不适用split
var simplifyPath = function (path) {
  const stack = [];
  let cur = "";

  path += "/"; // 为了最后一段
  for (const char of path) {
    if (char === "/") {
      // 处理token
      if (cur === "..") {
        if (stack.length) stack.pop();
      } else if (cur !== "." && cur !== "") {
        stack.push(cur);
      }
      cur = "";
    } else {
      cur += char;
    }
  }
  return "/" + stack.join("/");
};
