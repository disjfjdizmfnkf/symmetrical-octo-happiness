/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var addStrings = function(num1, num2) {
    let p1 = num1.length - 1, p2 = num2.length - 1;  //! 索引-1
    let res = ''
    let carry = 0;
    while (p1 >= 0 || p2 >= 0) {
        const digit1 = num1[p1] ? +num1[p1] : 0;
        const digit2 = num2[p2] ? +num2[p2] : 0;
        const sum = digit1 + digit2 + carry;
        carry = Math.floor(sum / 10);
        res = String(sum % 10) + res;
        //! while循环不要忘记条件更改
        p1--;
        p2--;
    }
    return carry ? '1' + res : res; 
};