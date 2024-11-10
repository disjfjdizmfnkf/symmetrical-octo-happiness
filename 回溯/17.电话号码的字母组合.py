class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                 "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        def backTrack(combination, remain_digits):
            if not remain_digits:
                res.append(combination)
                return
            for i in phone[remain_digits[0]]:  # 实际上就是遍历字符串
                backTrack(combination + i, remain_digits[1:])  # 上次组合的每个字符字符再和后面的数字的每个字符组合
        backTrack("", digits)
        return res