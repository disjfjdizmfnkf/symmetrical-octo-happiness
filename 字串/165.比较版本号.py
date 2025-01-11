class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i, j = 0, 0
        len1, len2 = len(version1), len(version2)
        while i < len1 or j < len2:
            num1 = 0
            while i < len1 and version1[i] != ".":
                num1 += num1 * 10 + int(version1[i])
                i += 1
            num2 = 0
            while j < len2 and version2[j] != ".":
                num2 += num2 * 10 + int(version2[j])
                j += 1
            i += 1
            j += 1
            if num1 != num2:
                return 1 if num1 > num2 else -1
        return 0
