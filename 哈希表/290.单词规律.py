
# 哈希表映射

# 一个哈希表中 一个作为键一个作为值映射
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        hashMap = {}

        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            if parrtern[i] in hashMap:
                return parrtern[i] == words[i]
            else:
                # Check if the word has already been mapped to another pattern character
                if words[i] in hashMap.value():
                    return False
                hashMap[parrtern[i]] = words[i]



# 两个哈希表把两个表的内容都映射到数字上
class Solution2:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        words_map = {}
        pattern_map = {}

        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            if words_map.get(words[i], 0) != pattern_map.get(pattern[i], 0):
                return False
            words_map[words[i]] = i + 1
            pattern_map[pattern[i]] = i + 1
        return True
