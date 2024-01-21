class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = []
        i, j = 0, 0
        while j < len(s):
            if s[j] != " ":
                j += 1
            else:
                words.append(s[i:j])
                while j < len(s) and s[j] == " ":
                    j += 1
                i = j
        words.append(s[i:j])  # 处理最后一个单词
        words = reversed(words)
        return " ".join(words)
    # split()用于将字符串分割成一个列表，它接受一个参为分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
    # strip()用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
    # join()用于将序列中的元素以指定的字符连接生成一个新的字符串