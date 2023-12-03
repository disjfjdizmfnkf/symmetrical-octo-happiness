class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashTable = {}
        for i in nums:
            if i not in hashTable:
                hashTable[i] = 1
            else:
                hashTable[i] += 1

        for k, v in hashTable.items():
            if v == 1:
                return k