class Solution:
    def isPalindrome(self, string):
        # 判断字符串是否是回文串
        return string == string[::-1]
    def partition(self, s: str) -> List[List[str]]:
        res = []
        l = len(s)
        def backTrack(combine, start):
            # 字符串分割完了，加入结果
            if start == l:
                res.append(combine)
                return
            # 从start位置开始分割字符串
            for i in range(start + 1, l + 1):
                spliced = s[start:i]
                if self.isPalindrome(spliced):  # 判断是否为回文串
                    backTrack(combine + [spliced], i)  # 递归调用
        backTrack([], 0)
        return res
