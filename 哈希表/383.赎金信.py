

# hashMap
class Solution1:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lib = {}

        for i in range(len(magazine)):
            lib[magazine[i]] = lib.get(magazine[i], 0) + 1

        for i in range(len(ransomNote)):
            lib[ransomNote[i]] = lib.get(ransomNote[i], 0) - 1
            if lib[ransomNote[i]] < 0:  # 注意边界情况 < 0才是不足 ==0 刚刚够用
                return False
        return True


# 统计字符个数
import collections
class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

    #collections.Counter()
    # 创建了一个计数器对象，用于统计 ransomNote 中每个字符的出现次数
    # - 号运算符应用于这两个计数器对象，会返回一个新的计数器对象，
    # 其中包含了 ransomNote 中字符出现次数与 magazine 中字符出现次数的差值。这意味着，
    # 如果 ransomNote 中的某个字符在 magazine 中出现的次数不足以构建 ransomNote，
    # 那么差值计数器中对应的字符出现次数将为负数。

## 此方法的Java版本




""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        if (ransomNote.length() > magazine.length()) {
            return false;
        }
        int[] cnt = new int[26];
        for (char c : magazine.toCharArray()) {
            cnt[c - 'a']++;                             # c-'a' 意味着26个英文字母(小写)索引 
        }
        for (char c : ransomNote.toCharArray()) {
            cnt[c - 'a']--;
            if(cnt[c - 'a'] < 0) {
                return false;
            }
        }
        return true;
    }
}

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""