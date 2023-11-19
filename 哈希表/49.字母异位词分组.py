# 两种方法没有太大的差别

# sorted(iterable, key=None, reverse=False)
# list.sort(key=None, reverse=False)
# list(iterable)   将可迭代对象转换成列表
# separator.join(iterable) separator是连接对象的分隔符
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for i in strs:  # 迭代的是列表对象
            sort_i = "".join(sorted(i))
            if sort_i in hashMap:
                hashMap[sort_i].append(i)
            else:
                hashMap[sort_i] = [i]
        return list(hashMap.values())


class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            count = [0] * 26  # a .... z
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]

        return list(res.values())