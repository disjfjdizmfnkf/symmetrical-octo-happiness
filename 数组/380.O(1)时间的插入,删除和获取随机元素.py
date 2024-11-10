from random import choice

# hashMap 帮助你在常数时间内获取某种关系

# hash表+数组
class RandomizedSet:

    def __init__(self):
        self._map = {}
        self._set = []

    def insert(self, val: int) -> bool:
        if val not in self._map:
            self._set.append(val)  # 不要搞错顺序
            self._map[val] = len(self._set) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self._map:
            remove_index = self._map[val]
            self._set[remove_index] = self._set[-1]
            self._map[self._set[remove_index]] = remove_index
            self._set.pop()
            del self._map[val]  # 清除字典中的val
            return True
        return False

    def getRandom(self) -> int:
        return choice(self._set)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()