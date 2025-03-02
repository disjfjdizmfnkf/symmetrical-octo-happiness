var MyStack = function () {
  this.length = 0;
  this.queue = [];
};

/**
 * @param {number} x
 * @return {void}
 */
MyStack.prototype.push = function (x) {
  this.queue.push(x);
  this.length++;
};

/**
 * @return {number}
 */
MyStack.prototype.pop = function () {
  if (!this.length) return null;
  //! 除了最后一个元素的所有元素先弹出队列再加入队列
  for (let i = 0; i < this.length - 1; i++) {
    const temp = this.queue.shift();
    this.queue.push(temp);
  }
  this.length--;
  return this.queue.shift(); // 弹出数组最后的元素实现LIFO
};

/**
 * @return {number}
 */
MyStack.prototype.top = function () {
  return this.queue[this.length - 1];
};

/**
 * @return {boolean}
 */
MyStack.prototype.empty = function () {
  return this.length === 0;
};

/**
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */
