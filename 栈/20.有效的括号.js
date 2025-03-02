/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const map = { '(': ')', '{': '}', '[': ']' };
    const stack = [];
    for (const char of s) {
        if (char in map) {
          stack.push(map[char]); 
        } else if (stack.length) { // 匹配到右括号时:
            if (stack.pop() !== char) {//* 栈中的和当前不匹配
                return false;
            }
        } else {//* 栈中没有括号匹配了
            return false;
        }
    }
    //* 如果还有括号没有被匹配也不算闭合
    return !stack.length;
};

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const map = { '(': ')', '{': '}', '[': ']' };
    const stack = [];
    for (const char of s) {
        if (char in map) {
            stack.push(char);
        } else {
            // 匹配到右括号时
            //! 栈中没有括号了
            //! 栈中的括号不匹配
            if (!stack.length || char !== map[stack.pop()]) return false;
        }

    }
    // 最后判断栈中是否有括号还没有被匹配 eg. 输入:"["
    return !stack.length;
};