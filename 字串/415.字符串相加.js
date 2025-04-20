/*         使用逻辑运算符赋值
*   || 返回第一个真值,如果没有则返回最后一个操作数
    let a = 0 || 2 || 3; // a 的值为 2，因为 2 是第一个真值
    let b = null || undefined || "hello"; // b 的值为 "hello"，因为 "hello" 是第一个真值
    let c = 0 || false || null; // c 的值为 null，因为没有真值，返回最后一个操作数
*   && 会返回第一个假值,如果没有则返回最后一个操作数
    let a = 1 && 2 && 3; // a 的值为 3，因为没有假值，返回最后一个操作数
    let b = 1 && 0 && 3; // b 的值为 0，因为 0 是第一个假值
    let c = null && "hello" && undefined; // c 的值为 null，因为 null 是第一个假值
*/
/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var addStrings = function(num1, num2) {
    let p1 = num1.length - 1, p2 = num2.length - 1;
    let res = ''
    let carry = 0;
    while (p1 >= 0 || p2 >= 0) {
        const digit1 = +num1[p1] || 0;
        const digit2 = +num2[p2] || 0;
        const sum = digit1 + digit2 + carry;
        carry = Math.floor(sum / 10);
        res = String(sum % 10) + res;
        //! while循环不要忘记条件更改
        p1--;
        p2--;
    }
    return carry ? '1' + res : res; //! 考虑最后的进位
};