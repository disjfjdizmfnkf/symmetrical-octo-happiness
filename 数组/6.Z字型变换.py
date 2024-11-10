class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        L = [""] * numRows
        t = (numRows - 1) * 2
        for i in range(len(s)):
            p = i % t
            if p >= numRows:
                L[t - p] += s[i]
            else:
                L[p] += s[i]

        return "".join(L)

    #  "".join()是一个字符串方法，用""中的内容连接并返回一个字符串,
    #  （）中的内容是一个可迭代对象，比如列表，元组，字符串等
