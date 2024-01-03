class Solution1:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backTrack(combine, l_brackets, r_brackets, n):
            if r_brackets > l_brackets:
                return
            if r_brackets == n:
                res.append(combine)
            # 在递归调用中 combine + "(" 实际上是new_combine = combine + "("
            # 创建了一个新的字符串，而不是在原有的字符串上修改，所以会消耗更多的内存
            backTrack(combine + "(", l_brackets + 1, r_brackets, n)
            backTrack(combine + ")", l_brackets, r_brackets + 1, n)

        backTrack("", 0, 0, n)
        return res


class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        # 使用列表来模拟栈，pop()和append()操作
        # 递归的时候用列表作为combine，这样在递归调用的时候不会再创建新的字符串
        def backTrack(combine, l_brackets, r_brackets):
            if r_brackets == n:
                res.append("".join(combine))
            if r_brackets < l_brackets:
                combine.append(')')
                backTrack(combine, l_brackets, r_brackets + 1)
                combine.pop()
            if l_brackets < n:
                combine.append('(')
                backTrack(combine, l_brackets + 1, r_brackets)
                combine.pop()

        backTrack([], 0, 0)
        return res