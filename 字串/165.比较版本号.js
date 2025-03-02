/**
 * @param {string} version1
 * @param {string} version2
 * @return {number}
 */
//* 使用数字解决前导0的问题
var compareVersion = function(version1, version2) {
    let num1, num2;
    let p1 = 0, p2 = 0;
    let len1 = version1.length, len2 = version2.length;
    while (p1 < len1 || p2 < len2) {
        num1 = 0;
        while (p1 < len1 && version1[p1] !== '.') {
            num1 = num1 * 10 + +version1[p1];
            p1++;
        }
        num2 = 0;
        while (p2 < len2 && version2[p2] !== '.') {
            num2 = num2 * 10 + +version2[p2];
            p2++;
        }
        p1++;
        p2++;
        if (num1 !== num2) {
            return num1 > num2 ? 1 : -1;
        }
    }
    return 0
};