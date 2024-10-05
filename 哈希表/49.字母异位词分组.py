# 两种方法没有太大的差别

# sorted(iterable, key=None, reverse=False)
# list.sort(key=None, reverse=False)
# list(iterable)   将可迭代对象转换成列表
# separator.join(iterable) separator是连接对象的分隔符
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 将所有·同分异构·项 重构为一个相同的标签作为分类
        hashMap = {}
        for i in strs:
            # python中的字符串是可迭代对象，sorted会将其转换为列表，join方法将列表再连接成新字符串
            sorted_i = "".join(sorted(i))
            if sorted_i in hashMap:
                hashMap[sorted_i].append(i)
            else:
                hashMap[sorted_i] = [i]
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