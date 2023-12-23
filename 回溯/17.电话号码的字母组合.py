class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                 "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        def backTrack(combinations, next):
            if not next:
                res.append(combinations)
                return
            for i in phone[next[0]]:
                backTrack(combinations + i, next[1:])

        backTrack("", digits)
        return res