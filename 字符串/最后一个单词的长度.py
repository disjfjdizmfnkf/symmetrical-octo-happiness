

#遍历 只记录目前最后的单词长度
class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        currWordLen = 0
        for i in range(len(s)):
            if s[i] != " ":
                if s[i-1]  == " ":
                    currWordLen = 0 
                currWordLen += 1
        return currWordLen