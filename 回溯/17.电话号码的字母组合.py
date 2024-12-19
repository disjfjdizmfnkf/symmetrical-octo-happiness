class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        #  num -> chars    index -> chars    使用数组比字典高效
        mapping = ['', '', 'abc', 'def', 'ghi',
                   'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = []

        def backTrack(combination, remainDigits):
            if not remainDigits:
                res.append(combination)
                return
            # remainDigits是字符串，作为索引时需要转换为数字
            currentDigit = int(remainDigits[0])
            for char in mapping[currentDigit]:
                backTrack(combination + char, remainDigits[1:])

        backTrack('', digits)
        return res
