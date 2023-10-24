
# hash表+数组
class RandomizedSet:

    def __init__(self):
        self.Map = {}  # 存储bucket中的数和它的下标
        self.bucket = []

    def insert(self, val: int) -> bool:
        if val not in self.Map:
            self.bucket.append(val)
            self.Map[val] = len(self.bucket) - 1
            return True
        return False

    def remove(self, val: int) -> bool:  # 用最后一个元素覆盖要删除的数，再把最后一个删了
        if val in self.Map:
            r_index = self.Map[val]
            self.bucket[r_index] = self.bucket[-1]
            self.Map[self.bucket[r_index]] = r_index
            self.bucket.pop()
            del self.Map[val]
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.bucket)  # 随机获取元素

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()