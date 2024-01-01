class Solution1:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backTrack(combine, l_brackets, r_brackets, n):
            if r_brackets > l_brackets:
                return
            if r_brackets == n:
                res.append(combine)
            backTrack(combine + "(", l_brackets + 1, r_brackets, n)
            backTrack(combine + ")", l_brackets, r_brackets + 1, n)

        backTrack("", 0, 0, n)
        return res