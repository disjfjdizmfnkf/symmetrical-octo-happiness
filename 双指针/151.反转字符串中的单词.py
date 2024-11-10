class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split() # 接受一个参数作为分隔符，默认空格换行等
        # return " ".join(words[::-1])
        l, r = 0, len(words) - 1
        while l < r:
            words[l], words[r] = words[r], words[l]
            l += 1
            r -= 1
        return ' '.join(words)
    # split()用于将字符串分割成一个列表，它接受一个参为分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
    # strip()用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
    # join()用于将序列中的元素以指定的字符连接生成一个新的字符串