
# hashMap
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashMap = {}
        for i in s:
            hashMap[i] = hashMap.get(i, 0) + 1
        for i in t:
            if i not in hashMap:
                return False
            else:
                hashMap[i] = hashMap.get(i, 0) - 1
        for v in hashMap.values():
            if v != 0:
                return False
        return True